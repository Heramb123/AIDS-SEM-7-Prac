import nltk
import pandas as pd
import numpy as np
from collections import Counter
from tabulate import tabulate
nltk.download('punkt')

from nltk import word_tokenize
from nltk.util import ngrams

text = "In a galaxy far, far away, aliens discovered the secret of time travel."

words = word_tokenize(text)

unigrams = words
bigrams = list(ngrams(words, 2))
trigrams = list(ngrams(words, 3))

print("Unigrams (1-grams):")
print(unigrams)

print("\nBigrams (2-grams):")
print(bigrams)

print("\nTrigrams (3-grams):")
print(trigrams)
