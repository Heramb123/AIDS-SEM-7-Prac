def is_english_word(word):
    return all(65 <= ord(char) <= 122 for char in word if char.isalpha())

def filter_english_words(text):
    words = text.split()
    english_words = [word for word in words if is_english_word(word)]
    return english_words

regional_text = "तुम  Nearby Market से Milk and Vegetables  लेकर आओ |"
english_words = filter_english_words(regional_text)
print(english_words)