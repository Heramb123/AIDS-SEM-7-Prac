import re

sentence = "The quick brown fox jumps over the lazy dog"

tokens = re.findall(r'\b\w+\b', sentence)

print("Tokens:")
print(tokens)

print('\n')
print("{:<15} {:<10}".format("Word", "POS Tag"))
print("-" * 25)

for word in tokens:
    # Define simple rules for part-of-speech tagging
    if word.lower() in ["the", "a", "an"]:
        pos_tag = "DT"  # Determiner
    elif word.isalpha() and word[0].isupper():
        pos_tag = "NNP"  # Proper Noun
    elif word.isalpha() and word.endswith("s"):
        pos_tag = "NNS"  # Plural Noun
    elif word.isalpha():
        pos_tag = "NN"  # Noun
    else:
        pos_tag = "UNKNOWN"

    print("{:<15} {:<10}".format(word, pos_tag))