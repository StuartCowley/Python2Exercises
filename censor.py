def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)
    return result

def user():
    phrase = input("Feed me the dirty phrase you want cleaning up: ")
    block = input("Enter the word you want censoring: ")
    print(censor(phrase, block))

user()
