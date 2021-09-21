# a simple number guessing game

import random

def game(total_turns = 10, highest = random.randint(100, 1000)):
    '''Main game function'''

    print(f"========== Guess the number between 0 to {highest} ==========")

    to_guess = random.randint(0, highest)    # the number to guess
    turns_left = total_turns

    while turns_left:
        print(f"\n<=== You have {turns_left} turns left ===>")    # showing the left turns

        try:    # if the user enters anything except int, it will not raise any error and let the user continue the game
            guess = int(input("Enter your guess : "))

            if guess == to_guess:
                print(f"\n<=== You got it in {total_turns - turns_left + 1} turns! ===>\n")
                return
            elif guess < to_guess:
                print("Too low!")
            else:
                print("Too high!")

            turns_left -= 1

        except:    # avoiding the error
            print("\n<=== Please enter a valid integer! ===>\n")

    # if the user failed to guess the correct answer
    print("\n<=== Sorry.. You have failed! ===>\n")


if __name__ == "__main__":
    # first game
    game()

    # asking if the user wants to play the game again
    while True:
        choice = input("\nWant to play again? (y/n) : ").lower()

        if choice == 'y':
            print()    # for printing a new line before next game
            game()
        elif choice == 'n':
            print("\n========== Thank you for playing the game! ==========")
            break
        else:
            print("\nPlease enter (y/n)\n")