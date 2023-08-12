import random

def guess_the_dice():
    target = random.randint(1,6)
    attemps = 3

    print("Welcome to Guess the Dice!")
    print("I have chosen a number between 1 to 6. Can you guess it in 3 attemps?")

    while attemps > 0:
        guess = int(input("Enter youe guess: "))

        if guess == target:
            print("Congratulation! You guess it right!")
            break
        else:
            attemps = attemps-1
            if attemps > 0:
                print(f"Wrong guess. You have {attemps} attemps left.")
            else:
                print(f"Sorry, you're out of attemps. The correct number was {target}.")

if __name__ == "__main__":
    guess_the_dice()