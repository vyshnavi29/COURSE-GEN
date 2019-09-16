import re
import sys
from utils import write_status
import nltk


def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    stop_words = [
    "a", "about", "above", "across", "after", "afterwards", 
    "again", "all", "almost", "alone", "along", "already", "also",    
    "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "as", "at", "be", "became", "because", "become","becomes", "becoming", "been", "before", "behind", "being", "beside", "besides", "between", "beyond", "both", "but", "by","can", "cannot", "cant", "could", "couldnt", "de", "describe", "do", "done", "each", "eg", "either", "else", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "find","for","found", "four", "from", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "i", "ie", "if", "in", "indeed", "is", "it", "its", "itself", "keep", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mine", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next","no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part","perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "she", "should","since", "sincere","so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "take","than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they",
    "this", "those", "though", "through", "throughout","im",
    "thru", "thus", "to", "together", "too", "toward", "towards",
    "under", "until", "up", "upon", "us",
    "very", "was", "we", "well", "were", "what", "whatever", "when",
    "whence", "whenever", "where", "whereafter", "whereas", "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", 
    "who", "whoever", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves"
    ]
    if word in stop_words:
        word=""
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


def handle_emojis(review):
    # Smile -- :), : ), :-), (:, ( :, (-:, :') ,<:o)
    review = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|\<:o\))', ' EMO_POS ', review)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D ,:p
    review = re.sub(r'(:\s?D|:-D|x-?D|X-?D|:p)', ' EMO_POS ', review)
    # Love -- <3, :*
    review = re.sub(r'(<3|:\*)', ' EMO_POS ', review)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    review = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', review)
    # Confused -- :-S , :s ,:S
    review = re.sub(r'(:-?(s|S))', ' EMO_NEG ', review)
    # Sad -- :-(, : (, :(, ):, )-:, :'(, :] ,:-|
    review = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:|:\'\(|:\]|:-\|)', ' EMO_NEG ', review)
    # Cry -- :,(, :'(, :"(
    review = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', review)
    return review


def preprocess_review(review):
    processed_review = []
    # Convert to lower case
    review = review.lower()
    # Replaces URLs with the word URL
    review = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', review)
    # Replace @handle with the word USER_MENTION
    review = re.sub(r'@[\S]+', 'USER_MENTION', review)
    # Replaces #hashtag with hashtag
    review = re.sub(r'#(\S+)', r' \1 ', review)
    # Remove RT (rereview)
    review = re.sub(r'(\brt\b|&[\S])', '', review)
    # Replace 2+ dots with space
    review = re.sub(r'\.{2,}', ' ', review)
    # Strip space, " and ' from review
    review = review.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    review = handle_emojis(review)
    # Replace multiple spaces with a single space
    review = re.sub(r'\s+', ' ', review)
    words = review.split()

    for word in words:
        word = preprocess_word(word)
        if is_valid_word(word):
            if use_stemmer:
                word = str(porter_stemmer.stem(word))
            processed_review.append(word)

    return ' '.join(processed_review)


def preprocess_csv(csv_file_name, processed_file_name, test_file):
    save_to_file = open(processed_file_name, 'w')

    with open(csv_file_name, 'r') as csv:
        lines = csv.readlines()
        total = len(lines)
        #print(lines," ",total)
        for i, line in enumerate(lines):
            #print(i,line)
            review_id = line[:line.find(',')]
            #print(review_id,test_file)
            if not test_file:
                line = line[1 + line.find(','):]
                positive = int(line[:line.find(',')])
                #print(positive)
            line = line[1 + line.find(','):]
            review = line
            #print(review)
            processed_review = preprocess_review(review)
            #print("hello",processed_review)
            if not test_file:
                save_to_file.write('%s,%d,%s\n' %
                                   (review_id, positive, processed_review))
            else:
                save_to_file.write('%s,%s\n' %
                                   (review_id, processed_review))
            write_status(i + 1, total)
    save_to_file.close()
    print('\nSaved processed reviews to: %s' % processed_file_name)
    return processed_file_name


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python preprocess.py <raw-CSV>')
        exit()
    use_stemmer = False
    csv_file_name = sys.argv[1]
    processed_file_name = sys.argv[1][:-4] + '-processed.csv'
    print(processed_file_name)
    preprocess_csv(csv_file_name, processed_file_name, test_file=True)