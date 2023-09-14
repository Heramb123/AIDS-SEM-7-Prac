import nltk
from nltk.stem import SnowballStemmer, LancasterStemmer

snowball_stemmer = SnowballStemmer("english")
lancaster_stemmer = LancasterStemmer()

words = ["running", "flies", "happily", "agreed", "owned", "jumps", "stemming", "stemmer"]

print("\nSnowball Stemmer:")
for word in words:
    stemmed_word = snowball_stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")

print("\nLancaster Stemmer:")
for word in words:
    stemmed_word = lancaster_stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")