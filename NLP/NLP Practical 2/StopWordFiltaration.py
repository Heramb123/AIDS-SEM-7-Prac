def filter_stop_words(text, stop_words):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

input_text = "This is a sample paragraph with some common English stop words. It demonstrates how to filter them out."
custom_stop_words = ["this", "is", "a", "with", "how", "to", "them", "out"]
filtered_text = filter_stop_words(input_text, custom_stop_words)
print(filtered_text)