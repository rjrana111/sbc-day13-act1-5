def process_sentece(input_text):
    sentence_endings = {'.', '!', '?'}
    sentences = []
    current_sentence = []
    
    for char in text:
        current_sentence.append(char)
        if char in sentence_endings:
            sentences.append(''.join(current_sentence).strip())
            current_sentence = []
    
    if current_sentence:
        sentences.append(''.join(current_sentence).strip())
    
    return sentences

text = "Hello! How are you? I'm doing fine."
input_text = input("Enter a text: ")
sentences = process_sentece(text)
print(sentences)
