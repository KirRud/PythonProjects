import os


answer = input("Work?(Y/N)").lower()
if answer == "y":
    print("Your capabilities:")
    print("1 - Learn")
    print("2 - Develop yourself")
    print("3 - Work with your team")
    answer1 = int(input("Your choise?"))
    if answer1 == 1:
        print("Okey, learning")
        print(os.listdir())
    elif answer1 == 2:
        print("Developing yourself")
    elif answer1 == 3:
        print("Okey, working")
    else:
        print("Wrong anwser")
elif answer == "n":
    print("Bye")
else:
    print("Wrong answer")