import nltk
from nltk import word_tokenize, pos_tag
sentence = "The quick brown fox jumps over the lazy dog" tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens) print("Tokens:") print(tokens)
pos_tags = pos_tag(tokens) print('\n')
print("{:<15} {:<10}".format("Word", "POS Tag")) print("-" * 25)
for word, pos in pos_tags:
print("{:<15} {:<10}".format(word, pos))
