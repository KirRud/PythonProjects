import random

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
             'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]
print(secret_word)

while True:
    letter = input("Enter latter  ")
    if len(letter) != 1:
        continue
    if (letter in secret_word):
        print(letter)
    else:
        print("No letter")