import random
import threading
import os

#each line contains one word
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def shuffle_word(word):
    char_list = list(word)
    random.shuffle(char_list)
    return ''.join(char_list)

def timer(seconds):
    threading.Event().wait(seconds) #wait
    time_up_event.set() #signal that time is up
    print("Time's up!")


words = load_dictionary("5_letter_words.txt")
secret_word = random.choice(words)

print("The shuffled word is: ", shuffle_word(secret_word))
print("Rearrange the letters to form the correct word: ")

time_up_event = threading.Event()
threading.Thread(target=timer, args=(30,), daemon=True).start() #daemon -> quit if nothing else is running or keep it running

ok = False
while not time_up_event.is_set():
    word = input()
    if word == secret_word:
        ok = True
        break

if time_up_event.is_set(): #check if time is up
    print("You ran out of time!")
if ok:
    print("Correct! You guessed it! ", secret_word)
else:
    print("Not the right word, the correct one was: ", secret_word)



