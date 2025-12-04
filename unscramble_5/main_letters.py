import random
import threading
import queue
import time
import os
import sys # sys.exit(1) instead of exit()

"""
checklist of what to improve:
   - missing feedback if the user's input is incorrect (the program just loops silently)
   - better feedback and instructions or other output messages (eg. it's about 5 letter words - should be the first message)
   - complete the documentation (update README.md)
"""

#each line contains one word
def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            words = [line.strip() for line in f]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found")
        sys.exit(1) # exit with status 1 - indicating an error

def shuffle_word(word):
    char_list = list(word)
    random.shuffle(char_list)
    return ''.join(char_list)

def input_thread():
    while not time_up_event.is_set():
        try:
            user_input = input()
        except EOFError:
            break
        input_queue.put(user_input)

def timer(seconds):
    time.sleep(seconds)
    time_up_event.set()
    print("\nTime's up!")


words = load_dictionary("5_letter_words_.txt")
secret_word = random.choice(words)

print("The shuffled word is: ", shuffle_word(secret_word))
print("Rearrange the letters to form the correct word: ")

time_up_event = threading.Event()
input_queue = queue.Queue()
threading.Thread(target=input_thread).start()
threading.Thread(target=timer, args=(30,), daemon=True).start() #daemon -> quit if nothing else is running or keep it running

ok = False
# multiple guesses allowed
while not time_up_event.is_set():
    try:
        raw_input = input_queue.get_nowait() #remove the extra spaces and make the word lowercase
        word = raw_input.strip().lower()
        if not word.isalpha() or len(word) != 5:
            print("Please write a five letter word and press enter.")
            continue # allow for the user to correct themselves

        if word == secret_word:
            ok = True
            break
    except queue.Empty:
        time.sleep(0.05)

if time_up_event.is_set() and not ok: #check if time is up
    print("You ran out of time!")
if ok:
    print("Correct! You guessed it! ", secret_word)
else:
    print("Not the right word, the correct one was: ", secret_word)

#forcing the program to exit
os._exit(0)

