import re
from collections import Counter
from tabulate import tabulate

text = "In a galaxy far, far away, aliens discovered the secret of time travel."
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

tokens = [re.findall(r'\w+', sentence.lower()) for sentence in sentences]

flat_tokens = [word for sentence_tokens in tokens for word in sentence_tokens]
unique_words = list(set(flat_tokens))

unigram_counter = Counter(flat_tokens)

matrix_size = len(unique_words)
matrix = [[0] * matrix_size for _ in range(matrix_size)]
word_to_index = {word: index for index, word in enumerate(unique_words)}

for i in range(len(flat_tokens) - 1):
    word1, word2 = flat_tokens[i], flat_tokens[i + 1]
    index1, index2 = word_to_index[word1], word_to_index[word2]
    matrix[index1][index2] += 1 / unigram_counter[word1]

header = [''] + unique_words
matrix_with_headers = [[unique_words[i]] + matrix[i] for i in range(matrix_size)]

print("\nBigram Probability Table:")
print(tabulate(matrix_with_headers, headers=header, tablefmt='grid'))
