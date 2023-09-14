def simple_tokenization(text):

    words = text.split()
    return words

input_text = "Hello, this is an example sentence. How are you?"
tokens = simple_tokenization(input_text)
print(tokens)