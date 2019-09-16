from nltk import FreqDist
import pickle
import sys
from utils import write_status
from collections import Counter


# Takes in a preprocessed CSV file and gives statistics
# Writes the frequency distribution of words and bigrams
# to pickle files.


def analyze_review(review):
    result = {}
    result['MENTIONS'] = review.count('USER_MENTION')
    result['URLS'] = review.count('URL')
    result['POS_EMOS'] = review.count('EMO_POS')
    result['NEG_EMOS'] = review.count('EMO_NEG')
    review = review.replace('USER_MENTION', '').replace(
        'URL', '')
    words = review.split()
    result['WORDS'] = len(words)
    bigrams = get_bigrams(words)
    result['BIGRAMS'] = len(bigrams)
    return result, words, bigrams


def get_bigrams(review_words):
    bigrams = []
    num_words = len(review_words)
    for i in range(num_words - 1):
        bigrams.append((review_words[i], review_words[i + 1]))
    return bigrams


def get_bigram_freqdist(bigrams):
    freq_dict = {}
    for bigram in bigrams:
        if freq_dict.get(bigram):
            freq_dict[bigram] += 1
        else:
            freq_dict[bigram] = 1
    counter = Counter(freq_dict)
    return counter


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(len(sys.argv),' Usage: python stats.py <preprocessed-CSV>')
        exit()
    num_reviews, num_pos_reviews, num_neg_reviews = 0, 0, 0
    num_mentions, max_mentions = 0, 0
    num_emojis, num_pos_emojis, num_neg_emojis, max_emojis = 0, 0, 0, 0
    num_urls, max_urls = 0, 0
    num_words, num_unique_words, min_words, max_words = 0, 0, 1e6, 0
    num_bigrams, num_unique_bigrams = 0, 0
    all_words = []
    all_bigrams = []
    with open(sys.argv[1], 'r') as csv:
        lines = csv.readlines()
        num_reviews = len(lines)
        for i, line in enumerate(lines):
            t_id, if_pos, review = line.strip().split(',')
            if_pos = int(if_pos)
            if if_pos:
                num_pos_reviews += 1
            else:
                num_neg_reviews += 1
            result, words, bigrams = analyze_review(review)
            num_mentions += result['MENTIONS']
            max_mentions = max(max_mentions, result['MENTIONS'])
            num_pos_emojis += result['POS_EMOS']
            num_neg_emojis += result['NEG_EMOS']
            max_emojis = max(
                max_emojis, result['POS_EMOS'] + result['NEG_EMOS'])
            num_urls += result['URLS']
            max_urls = max(max_urls, result['URLS'])
            num_words += result['WORDS']
            min_words = min(min_words, result['WORDS'])
            max_words = max(max_words, result['WORDS'])
            all_words.extend(words)
            num_bigrams += result['BIGRAMS']
            all_bigrams.extend(bigrams)
            write_status(i + 1, num_reviews)
    num_emojis = num_pos_emojis + num_neg_emojis
    unique_words = list(set(all_words))
    with open(sys.argv[1][:-4] + '-unique.txt', 'w') as uwf:
        uwf.write('\n'.join(unique_words))
    num_unique_words = len(unique_words)
    num_unique_bigrams = len(set(all_bigrams))
    print('\nCalculating frequency distribution')
    # Unigrams
    freq_dist = FreqDist(all_words)
    pkl_file_name = sys.argv[1][:-4] + '-freqdist.pkl'
    with open(pkl_file_name, 'wb') as pkl_file:
        pickle.dump(freq_dist, pkl_file)
    print('Saved uni-frequency distribution to %s' % pkl_file_name)
    # Bigrams
    bigram_freq_dist = get_bigram_freqdist(all_bigrams)
    bi_pkl_file_name = sys.argv[1][:-4] + '-freqdist-bi.pkl'
    with open(bi_pkl_file_name, 'wb') as pkl_file:
        pickle.dump(bigram_freq_dist, pkl_file)
    print('Saved bi-frequency distribution to %s' % bi_pkl_file_name)
    print('\n[Analysis Statistics]')
    print('reviews => Total: %d, Positive: %d, Negative: %d' % (num_reviews, num_pos_reviews, num_neg_reviews))
    print('User Mentions => Total: %d, Avg: %.4f, Max: %d' % (num_mentions, num_mentions / float(num_reviews), max_mentions))
    print('URLs => Total: %d, Avg: %.4f, Max: %d' % (num_urls, num_urls / float(num_reviews), max_urls))
    print('Emojis => Total: %d, Positive: %d, Negative: %d, Avg: %.4f, Max: %d' % (num_emojis, num_pos_emojis, num_neg_emojis, num_emojis / float(num_reviews), max_emojis))
    print('Words => Total: %d, Unique: %d, Avg: %.4f, Max: %d, Min: %d' % (num_words, num_unique_words, num_words / float(num_reviews), max_words, min_words))
    print('Bigrams => Total: %d, Unique: %d, Avg: %.4f' % (num_bigrams, num_unique_bigrams, num_bigrams / float(num_reviews)))