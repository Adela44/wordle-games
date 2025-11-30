import random

"""

# ANSI color codes
GREEN = "\033[32m"
ORANGE = "\033[33m"  # usually yellow/orange-ish
RESET = "\033[0m"

"""

#each line contains one word
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return guess in guesses #we check if the word exists in the list and has 5 letters

def evaluate_guess(guess, word):  #we return green/yellow or grey letters
    str = ""
    for i in range(5):
        if guess[i] == word[i]: #if it's in the correct location
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word: #if the word contains the correct letter
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i] #the normal color, greyish
    return str + "\033[0m"


def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5 letter word.")
    secret_word = random.choice(answers)
    attempts = 1
    max_attempts = 6
    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower() #makes the letter lowercase anyways
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English Word with 5 letters.")
            continue
        if guess == secret_word: # the correct guess
            print("You guessed the word! Congratulations! ",secret_word)
            break
        attempts += 1 #else continue with the attempts
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
        if attempts > max_attempts:
            print("Too many attempts. The secret word was: " + secret_word)


guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")
wordle(guesses, answers)