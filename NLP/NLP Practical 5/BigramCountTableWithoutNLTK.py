import re
from collections import Counter
from tabulate import tabulate
text = "In a galaxy far, far away, aliens discovered the secret of time travel."
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
tokens = [re.findall(r'\w+', sentence.lower()) for sentence in sentences]
flat_tokens = [word for sentence_tokens in tokens for word in sentence_tokens]
unique_words = list(set(flat_tokens)
bigrams = list(zip(flat_tokens[:-1], flat_tokens[1:]))
bigram_counter = Counter(bigrams)
matrix_size = len(unique_words)
matrix = [[0] * matrix_size for _ in range(matrix_size)]
word_to_index = {word: index for index, word in enumerate(unique_words)}
for bigram, count in bigram_counter.items():
    word1, word2 = bigram
    index1 = word_to_index[word1]
    index2 = word_to_index[word2]
    matrix[index1][index2] = count
header = [''] + unique_words
matrix_with_headers = [[unique_words[i]] + matrix[i] for i in range(matrix_size)]
print("\nBigram Count Table:")
print(tabulate(matrix_with_headers, headers=header, tablefmt='grid'))
