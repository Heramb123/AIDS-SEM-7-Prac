text = "In a galaxy far, far away, aliens discovered the secret of time travel"

sentences = nltk.sent_tokenize(text)
tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
flat_tokens = [word.lower() for sentence_tokens in tokens for word in sentence_tokens]
unique_words = list(set(flat_tokens))

bigrams = list(nltk.bigrams(flat_tokens))
unigram_counter = Counter(flat_tokens)
matrix_size = len(unique_words)
matrix = [[0] * matrix_size for _ in range(matrix_size)]
word_to_index = {word: index for index, word in enumerate(unique_words)}

for bigram in bigrams:
    word1, word2 = bigram
    index1 = word_to_index[word1]
    index2 = word_to_index[word2]
    matrix[index1][index2] += 1

header = [''] + unique_words
matrix_with_headers = [[unique_words[i]] + matrix[i] for i in range(matrix_size)]

print("\nBigram Count Table:")
print(tabulate(matrix_with_headers, headers=header, tablefmt='grid'))

