from string import punctuation
from hazm import word_tokenize,sent_tokenize, stopwords_list, Normalizer
import math
import numpy as np
import networkx as nx
from nltk.cluster.util import cosine_distance

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

def calculate_sentence_similarity(sentence1, sentence2):
  words1 = [word for word in word_tokenize(sentence1)]
  words2 = [word for word in word_tokenize(sentence2)]
  
  all_words = list(set(words1 + words2))
  
  vector1 = [0] * len(all_words)
  vector2 = [0] * len(all_words)
  
  for word in words1:
    vector1[all_words.index(word)] += 1
  for word in words2:
    vector2[all_words.index(word)] += 1

  return 1 - cosine_distance(vector1, vector2)

def calculate_similarity_matrix(sentences):
  similarity_matrix = np.zeros((len(sentences), len(sentences)))
  for i in range(len(sentences)):
    for j in range(len(sentences)):
      if i == j:
        similarity_matrix[i][j] = 1
      similarity_matrix[i][j] = calculate_sentence_similarity(sentences[i], sentences[j])
  
  return similarity_matrix

def get_best_sentences(text, percentage = 0.25):
  original_sentences = [sentence for sentence in sent_tokenize(text)]
  sentences = [preprocess(original_sentence) for original_sentence in original_sentences]
  similarity_matrix = calculate_similarity_matrix(sentences)

  similarity_graph = nx.from_numpy_array(similarity_matrix)

  scores = nx.pagerank(similarity_graph)

  ordered_scores = sorted(((scores[i], sentence) for i, sentence in enumerate(original_sentences)), reverse=True)

  number_of_sentences = math.ceil(len(sentences) * percentage)

  best_sentences = []
  for i in range(number_of_sentences):
    best_sentences.append(ordered_scores[i][1])

  return best_sentences