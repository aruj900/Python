import art
import random
print(art.logo)
print("Welcome to number guessing game")
print("I am thinking of a number between 1 and 100.")

EASY = 10
HARD = 5

correct_answer = random.randint(1,100)
attempts = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = EASY
elif difficulty == "hard":
    attempts = HARD


while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    attempts -= 1 
    if user_guess < correct_answer:
        print("Too low")
        if attempts != 0:
            print("Guess again")
    elif user_guess > correct_answer:
        print("Too high")
        if attempts != 0:
            print("Guess again")
    else:
        print(f"You got it! The answer was {correct_answer}")
        break;

    
    

if attempts == 0:
    print("You've run out of guesses, you loose")