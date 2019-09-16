import utils
import random
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from scipy.sparse import lil_matrix
from sklearn.feature_extraction.text import TfidfTransformer

# Performs classification using Naive Bayes.

FREQ_DIST_FILE = 'samtrain-processed-freqdist.pkl'
BI_FREQ_DIST_FILE = 'samtrain-processed-freqdist-bi.pkl'
TRAIN_PROCESSED_FILE = 'samtrain-processed.csv'
TEST_PROCESSED_FILE = 'mytest-processed.csv'
TRAIN = True
UNIGRAM_SIZE = 15000
VOCAB_SIZE = UNIGRAM_SIZE
USE_BIGRAMS = True
if USE_BIGRAMS:
    BIGRAM_SIZE =10000
    VOCAB_SIZE = UNIGRAM_SIZE + BIGRAM_SIZE
FEAT_TYPE = 'presence'


def get_feature_vector(review):
    uni_feature_vector = []
    bi_feature_vector = []
    words = review.split()
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if unigrams.get(word):
            uni_feature_vector.append(word)
        if USE_BIGRAMS:
            if bigrams.get((word, next_word)):
                bi_feature_vector.append((word, next_word))
    if len(words) >= 1:
        if unigrams.get(words[-1]):
            uni_feature_vector.append(words[-1])
    return uni_feature_vector, bi_feature_vector


def extract_features(reviews, test_file, batch_size=500, feat_type='presence'):
    """returns features and labels"""
    num_batches = int(np.ceil(len(reviews) / float(batch_size)))
    #print(num_batches," ",batch_size)
    for i in range(num_batches):
        batch = reviews[i * batch_size: (i + 1) * batch_size]
        features = lil_matrix((batch_size, VOCAB_SIZE))
        labels = np.zeros(batch_size)
        for j, review in enumerate(batch):
            if test_file:
                review_words = review[1][0]
                review_bigrams = review[1][1]
            else:
                review_words = review[2][0]
                review_bigrams = review[2][1]
                labels[j] = review[1]
            if feat_type == 'presence':
                review_words = set(review_words)
                review_bigrams = set(review_bigrams)
            for word in review_words:
                idx = unigrams.get(word)
                if idx>=0:
                    features[j, idx] += 1
            if USE_BIGRAMS:
                for bigram in review_bigrams:
                    idx = bigrams.get(bigram)
                    if idx:
                        features[j, UNIGRAM_SIZE + idx] += 1
        yield features, labels


def process_reviews(csv_file, test_file):
    """Returns a list of tuples of type (review_id, feature_vector)
            or (review_id, sentiment, feature_vector)"""
    reviews = []
    print('Generating feature vectors')
    with open(csv_file, 'r') as csv:
        lines = csv.readlines()
        total = len(lines)
        for i, line in enumerate(lines):
            if test_file:
                review_id, review = line.split(',')
            else:
                review_id, sentiment, review = line.split(',')
            feature_vector = get_feature_vector(review)
            #print(feature_vector)
            if test_file:
                reviews.append((review_id, feature_vector))
            else:
                reviews.append((review_id, int(sentiment), feature_vector))
            utils.write_status(i + 1, total)
    print('\n')
    return reviews


if __name__ == '__main__':
    np.random.seed(1337)
    unigrams = utils.top_n_words(FREQ_DIST_FILE, UNIGRAM_SIZE)
    #print("\nunigrams\n",unigrams)
    if USE_BIGRAMS:
        bigrams = utils.top_n_bigrams(BI_FREQ_DIST_FILE, BIGRAM_SIZE)
    reviews = process_reviews(TRAIN_PROCESSED_FILE, test_file=False)
    #print("\nreviews\n",reviews)
    if TRAIN:
        train_reviews, val_reviews = utils.split_data(reviews)
    del reviews
    

    print('Extracting features & training batches')
    clf = MultinomialNB()
    batch_size = len(train_reviews)
    i = 1
    n_train_batches = int(np.ceil(len(train_reviews) / float(batch_size)))
    #print(n_train_batches)
    for training_set_X, training_set_y in extract_features(train_reviews, test_file=False, feat_type=FEAT_TYPE, batch_size=batch_size):
        utils.write_status(i, n_train_batches)
        #print("hello\n",training_set_X,training_set_y)
        i += 1
        clf.partial_fit(training_set_X, training_set_y, classes=[0, 1])
    print('\n')
    
    
    print("accuracy")
    correct, total = 0, len(val_reviews)
    i = 1
    batch_size = len(val_reviews)
    #print("len(val_reviews) ",len(val_reviews))
    n_val_batches = int(np.ceil(len(val_reviews) / float(batch_size)))
    for val_set_X, val_set_y in extract_features(val_reviews, test_file=False, feat_type=FEAT_TYPE, batch_size=batch_size):
        prediction = clf.predict(val_set_X)
        correct += np.sum(prediction == val_set_y)
        utils.write_status(i, n_val_batches)
        i += 1
    print('\nCorrect: %d/%d = %.4f %%' % (correct, total, correct * 100. / total))
    
    print('\nTesting')
    del train_reviews
    test_reviews = process_reviews(TEST_PROCESSED_FILE, test_file=True)
    batch_size=500
    n_test_batches = int(np.ceil(len(test_reviews) / float(batch_size)))
    #print("dvd",n_test_batches," ",batch_size)
    predictions = np.array([])
    print('Predicting batches')
    i = 1
    for test_set_X, _ in extract_features(test_reviews, test_file=True, feat_type=FEAT_TYPE):
        prediction = clf.predict(test_set_X)
        predictions = np.concatenate((predictions, prediction))
        utils.write_status(i, n_test_batches)
        i += 1
    predictions = [(str(j+1), int(predictions[j]))
                       for j in range(len(test_reviews))]
    #print(predictions)
    utils.save_results_to_csv(predictions, 'naivebayes.csv')
    print('\nSaved to naivebayes.csv')