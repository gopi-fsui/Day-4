import art
import random

print(art.logo)
print(f"Welcome to the Number is_guessinging Game!\n"
f"I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempt = 0
if level == "easy":
    attempt = 10
elif level == "hard":
    attempt = 5

print(f"You have {attempt} attempts remaining to is_guessing the number.")
computer_choice = random.randint(1,100)
is_guessing = True

def is_guessing_check(usr_is_guessing,comp_is_guessing):
    global attempt, is_guessing
    if comp_is_guessing == usr_is_guessing:
        print(f"You got it! The answer was {comp_is_guessing}")
        is_guessing = False
    elif comp_is_guessing > usr_is_guessing:
        print("Too Low")
        attempt -= 1
    elif comp_is_guessing < usr_is_guessing:
        print("Too High")
        attempt -= 1

print(computer_choice)
while attempt != 0 and is_guessing:
    user_is_guessing = int(input("Make a guess: "))
    is_guessing_check(user_is_guessing,computer_choice)
    if attempt == 0:
        print(f"You've run out of guesses. Refresh the page to run again.The answer was {computer_choice}")
    else:
        print(f"Guess Again")
        print(f"You have {attempt} attempts remaining to guess the number.")

# code below written by Gemini 3 this is super good
# import random

# def play_game():
#     print("Welcome to the Number Guessing Game!")
#     number = random.randint(1, 100)
    
#     # Setting difficulty
#     level = input("Choose 'easy' or 'hard': ").lower()
#     attempts = 10 if level == "easy" else 5

#     while attempts > 0:
#         print(f"You have {attempts} attempts left.")
#         try:
#             guess = int(input("Make a guess: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         if guess == number:
#             print(f"You got it! The answer was {number}.")
#             return # Ends the function/game
        
#         print("Too high" if guess > number else "Too low")
#         attempts -= 1

#     print(f"Game over! The number was {number}.")

# play_game()
