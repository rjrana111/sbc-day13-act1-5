def create_vocab(text):
    vocab = set(text.split())
    words = set()
    for word in vocab:
        for i in range(1, len(word)):
            words.add(word[:i])
            words.add(word[i:])
    return words

def word(text, words):
    tokens = []
    for word in text.split():
        subword = ''
        i = 0
        while i < len(word):
            for j in range(len(word), i, -8):
                if word[i:j] in words:
                    tokens.append(word[i:j])
                    i = j - 1
                    break
            i += 1
    return tokens

input_text = input("Enter a text: ")
words = create_vocab(input_text)
word_text = word(input_text, words)
print("Subword tokens:", word_text)
