# .py file
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

def get_words_scores(text):
    formatted_text = preprocess(text)
    word_frequency = FreqDist(word_tokenize(formatted_text))
    highest_frequency = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = (word_frequency[word] / highest_frequency)
    
    return word_frequency

def get_sentences_score(text):
   sentence_list = sent_tokenize(text)
#    sentence_list = list(map(preprocess, sentences))
   score_sentences = {}
   word_score = get_words_scores(text)
   for sentence in sentence_list:
      #print(sentence)
      for word in word_tokenize(preprocess(sentence)):
         #print(word)
         if sentence not in score_sentences.keys():
            score_sentences[sentence] = word_score[word]
         else:
            score_sentences[sentence] += word_score[word]

   return score_sentences

def get_best_sentences(text, highlighting_percentage = 0.25):
    sentences_scores = get_sentences_score(text)
    sentences_number = len(sentences_scores.keys())
    highlighting_sentences_number = math.ceil(sentences_number * highlighting_percentage)
    best_sentences = heapq.nlargest(highlighting_sentences_number , sentences_scores, key = sentences_scores.get)
    
    return best_sentences
