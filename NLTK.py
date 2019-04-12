import nltk
import nltk, re, string, collections
from nltk.book import *
from nltk import word_tokenize
from nltk.corpus import stopwords 
from nltk.util import ngrams
from collections import Counter
from string import punctuation
from nltk.collocations import *
print(len(text1))
print(len(text2))


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


#####**Text1###based on frequency
esBigrams1=[]
esBigrams1 = ngrams(text1, 2)
esBigram1Freq = collections.Counter(esBigrams1)
print("Most common bigrams based on frequency in text1 :",esBigram1Freq.most_common(20))
######**Text2#####based on frequency
esBigrams2=[]
esBigrams2 = ngrams(text2, 2)
esBigram2Freq = collections.Counter(esBigrams2)
print("Most common bigrams based on frequency in text2 :",esBigram2Freq.most_common(20))
################Remove stop words and punctuations in Text1##################################

stop_words = set(stopwords.words('english'))
filtered_sentence_text1 = [w for w in text1 if not w in stop_words]
filtered_text1=strip_punctuation(filtered_sentence_text1)
esBigrams1=[]
esBigrams1 = ngrams(filtered_text1, 2)
esBigram1Freq = collections.Counter(esBigrams1)
print("Most common bigrams based on frequency without stopwords and punctuations in text1 :",esBigram1Freq.most_common(20))

######################### Remove stop words and punctuations in Text2 ##################################

stop_words = set(stopwords.words('english'))
filtered_sentence_text2 = [w for w in text2 if not w in stop_words]
filtered_text2=strip_punctuation(filtered_sentence_text2)
esBigrams1=[]
esBigrams1 = ngrams(filtered_text2, 2)
esBigram1Freq = collections.Counter(esBigrams1)
print("Most common bigrams based on frequency without stopwords and punctuations in text2 :",esBigram1Freq.most_common(20))


####### top 20 word bigram collocations in text1 #####

stop_words = set(stopwords.words('english'))
filtered_sentence_text1 = [w for w in text1 if not w in stop_words]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(filtered_sentence_text1)
finder.apply_freq_filter(3)
print("top 20 word bigram collocations in text1",finder.nbest(bigram_measures.pmi, 20))


####### top 20 word bigram collocations in text2  #####

stop_words = set(stopwords.words('english'))
filtered_sentence_text2 = [w for w in text2 if not w in stop_words]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(filtered_sentence_text2)
finder.apply_freq_filter(3)
print(" top 20 word bigram collocations in text2",finder.nbest(bigram_measures.pmi, 20))
