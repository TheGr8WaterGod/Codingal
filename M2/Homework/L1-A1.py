import random

def play_game():
    secret_number = random.randint(1, 10)
    print("i am thinking of a number between 1 and 10")

    while True:
        guess = input("enter your guess ")

        if not guess.isdigit():
            print("please enter a valid number")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("correct you guessed the number")
            break
        else:
            print("wrong guess")
            try_again = input("do you want to try again yes or no ").strip().lower()
            if try_again != "yes":
                print("the correct number was " + str(secret_number))
                break

while True:
    play_game()
    replay = input("do you want to play a new game yes or no ").strip().lower()
    if replay != "yes":
        print("thanks for playing")
        break