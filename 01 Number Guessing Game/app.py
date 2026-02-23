#RANDOM NUMBER GENERATION
import random
number=random.randint(1,100) #1 TO 100 NUMBER RANGE

print("🎮 Welcome to the Number Guessing Game!")


#Number of Guess
attempts=0

#PREDICTION Statements
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess > number:
        print("Too High ! Try Again.")
    elif guess < number:
        print("Too Low ! Try Again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
