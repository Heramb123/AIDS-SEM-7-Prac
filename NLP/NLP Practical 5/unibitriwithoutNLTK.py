text = "In a galaxy far, far away, aliens discovered the secret of time travel."
words = text.split()

bigrams = [tuple(words[i:i+2]) for i in range(len(words) - 1)]
trigrams = [tuple(words[i:i+3]) for i in range(len(words) - 2)]

print("Unigrams (1-grams):")
print(words)

print("\nBigrams (2-grams):")
print(bigrams)

print("\nTrigrams (3-grams):")
print(trigrams)
