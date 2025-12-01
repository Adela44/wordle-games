import random
import threading


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
    threading.Event().wait(seconds)
    time_up_event.set()
    print("Time's up!")

time_up_event = threading.Event()
threading.Thread(target=timer, args=(30,), daemon=True).start()


words = load_dictionary("5_letter_words.txt")
secret_word = random.choice(words)

print("The shuffled word is: ", shuffle_word(secret_word))
print("Rearrange the letters to form the correct word: ")

word = input()

if time_up_event.is_set():
    print("You ran out of time!")
else:
    if word == secret_word:
        print("Correct! You guessed it! ", word)
    else:
        print("Not the right word, the correct one was: ", secret_word)



