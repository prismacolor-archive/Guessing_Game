import random
from random import randint

playing = True

def number_game():
    while True:
        print("Try to guess the correct number!")
        while playing:
            try:
                comp_guess = (randint(1, 9))
                user_guess = int(input("Please enter a number between 0 and 10: "))
            except:
                print("Please enter a number between 0 and 10: ")
                continue
            else:
                if user_guess == comp_guess:
                    print("You've guessed correctly!")
                else:
                    print("Sorry, that's not the right answer! The correct answer was", comp_guess)
            break   
                    
        gameover = input("Would you like to play again? Enter y or n.").lower()
        if gameover[0].lower()=='y':
            continue
        else:
            print("Thanks for playing!")
        break

number_game()