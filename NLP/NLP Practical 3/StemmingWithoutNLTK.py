def simple_stem(word):
    suffixes = ["ing", "ed", "ly", "es", "s"]

    for suffix in suffixes:
        if word.endswith(suffix):
            return word[: -len(suffix)]

    return word

# Test the simple stemmer
words = ["running", "flies", "happily", "agreed", "owned", "jumps", "stemming", "stemmer"]

for word in words:
    stemmed_word = simple_stem(word)
    print(f"{word} -> {stemmed_word}")
