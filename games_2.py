import random

MAX_ERRORS = 8
words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]
users_word = ["*"] * len(secret_word)  # string(слова) не изменяемы тип данных
errors_counter = 0

print(secret_word)
#print("".join(users_word))



def show_users_word(arg):
    print("".join(users_word))

# show_users_word(users_word)
# ord() return code of letter
while True:
    letter = input("Enter latter  ").lower()
    if len(letter) != 1 or not letter.isalpha(): # .isalpha возвращает true если слово состоит только из букв
        continue

    if (letter in secret_word):
        for position, char in enumerate(secret_word): #благодаря enumerate position присваивается номер текущего элемента
            if char == letter:
                users_word[position] = letter
        show_users_word(users_word)
        if '*' not in users_word:
            print("You win")
            break
    else:
        errors_counter += 1
        print(f"No letter, errors {errors_counter}")
        if (errors_counter == MAX_ERRORS):
            print("You loose")
            break

print("Game finished")
