word_list = []
input_text = input("Enter a word or sentence: ")

def process_words(input_text):
    word_list.extend(input_text.split())

process_words(input_text)


print(word_list)