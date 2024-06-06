from string import punctuation
from hazm import word_tokenize,sent_tokenize, stopwords_list, Normalizer
from nltk import FreqDist
import heapq
import math

def preprocess(text):
    normalizer = Normalizer()
    normalized_text = normalizer.normalize(text)
    tokens = []
    for token in word_tokenize(normalized_text):
        tokens.append(token)
    persian_punctuation = punctuation + '،؟ـ٫٬«»؛:-'
    tokens = [word for word in tokens if word not in stopwords_list() and word not in persian_punctuation]
    formatted_text = ' '.join(element for element in tokens)

    return formatted_text 

def get_top_n_words(text, n):
    words = [word for word in word_tokenize(preprocess(text))]
    frequency = FreqDist(words)
    top_n_words = [word[0] for word in frequency.most_common(n)]
    
    return top_n_words

def calculate_sentences_score(text, important_words, distance):
    original_sentences = [sentence for sentence in sent_tokenize(text)]
    sentences = list(map(preprocess, original_sentences))
    
    # print(f'important_words: {important_words}\ndistance: {distance}')
    # print('------------------------------------------------------------')
    # print('sentences:')
    # for sentence in sentences:
    #     print(sentence)
    
    # print('------------------------------------------------------------')
    
    scores = []
    sentence_index = 0

    for sentence in [word_tokenize(sentence) for sentence in sentences]:
        word_index = []
        for word in important_words:
            try:
                word_index.append(sentence.index(word))
            except ValueError:
                pass

        word_index.sort()

        if len(word_index) == 0:
            continue

        groups_list = []
        group = [word_index[0]]
        i = 1
        while i < len(word_index):
            if word_index[i] - word_index[i - 1] < distance:
                group.append(word_index[i])
            else:
                groups_list.append(group[:])
                group = [word_index[i]]
            i += 1
        groups_list.append(group)

        max_group_score = 0
        for group in groups_list:
            important_words_in_group = len(group)
            total_words_in_group = group[-1] - group[0] + 1
            score = 1.0 * important_words_in_group**2 / total_words_in_group

            if score > max_group_score:
                max_group_score = score

        scores.append((max_group_score, sentence_index))
        sentence_index += 1

    return scores

def get_best_sentences(text, number_of_important_words, distance, percentage):
    sentences = sent_tokenize(text)
    scores = calculate_sentences_score(text, get_top_n_words(text, number_of_important_words), distance)
    best_scores = heapq.nlargest(math.ceil(len(sentences) * percentage), scores)
    best_sentences = []
    for score, sentence_index in best_scores:
        best_sentences.append(sentences[sentence_index])
    
    return best_sentences