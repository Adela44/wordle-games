import random

"""

# ANSI color codes
GREEN = "\033[32m"
ORANGE = "\033[33m"  # usually yellow/orange-ish
RESET = "\033[0m"

"""

# each line contains one word
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return guess in guesses # check if the word exists in the guesses list

def evaluate_guess(guess, word):  # return green/yellow/grey letters accordingly
    str = ""
    n = len(guess)
    for i in range(n):
        if i < len(word) and guess[i] == word[i]: #if it's in the correct location
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word: # if the word contains the correct letter
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i] # the normal color, grey-ish
    return str + "\033[0m"


def wordle(guesses, answers):
    print("Welcome to Wordle Fruit Version! Get 5 chances to guess a fruit name.")
    secret_word = random.choice(answers)
    attempts = 1
    max_attempts = 5
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower() # makes the letter lowercase (in case of uppercase letters)
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter a Valid Fruit name.")
            continue
        if guess == secret_word: # the correct guess
            print("You guessed the word! Congratulations! ",secret_word)
            break
        attempts += 1 # else continue with the attempts
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
        if attempts > max_attempts:
            print("Too many attempts. The secret word was: " + secret_word)


guesses = load_dictionary("fruit_guesses.txt")
answers = load_dictionary("fruit_answers.txt")
wordle(guesses, answers)