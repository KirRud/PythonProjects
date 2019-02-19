import random

MAX_ERRORS = 8
words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада']


def show_users_word(arg):
    print("".join(users_word))



flg = True
while flg:
    secret_word = random.sample(words_list, 1)[0]
    users_word = ["*"] * len(secret_word)
    errors_counter = 0
    while True:
        letter = input("Enter latter  ").lower()
        if len(letter) != 1:
            continue

        if ord(letter) < 1072 or ord(letter) > 1103:
            print("Enter only russian letters")
            continue

        if (letter in secret_word):
            for position, char in enumerate(
                    secret_word):  # благодаря enumerate position присваивается номер текущего элемента
                if char == letter:
                    users_word[position] = letter
            show_users_word(users_word)
            if '*' not in users_word:
                print("You win")
                break
        else:
            errors_counter += 1
            print(f"No letter, errors number: {errors_counter}")
            if (errors_counter == MAX_ERRORS):
                print("You loose")
                break
    choose = input("More?(Y/N)").lower()
    if choose == "n":
        flg = False


print("Game finished")
