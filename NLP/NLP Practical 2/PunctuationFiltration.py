import re

input_text = "Hey there, it's a beautiful day! How's everything going?"

def filter_punctuation(text):

    filtered_text = re.sub(r'[^\w\s]', '', text)
    return filtered_text

filtered_text = filter_punctuation(input_text)
print(filtered_text)
