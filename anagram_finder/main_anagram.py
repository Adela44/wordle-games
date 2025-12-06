import sys
from collections import defaultdict

def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            words = [line.strip() for line in f]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

"""
    Obs: We sort the letters because words that are anagrams always have the same letter,
    just in different order -> we can use the sorted word as a key, to group the anagrams 
    together
"""

def generate_anagram_groups(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))  #eg. sorted("listen") -> ['e', 'i', 'l', 'n', 's', 't']
        groups[key].append(word)

    # Keep only groups with more than one anagram
    filtered = {}
    for key, word_list in groups.items():
        if len(word_list) > 1:
            filtered[key] = word_list

    return filtered

words = load_dictionary("5-letter-words.txt")
anagrams = generate_anagram_groups(words)
for key, group in anagrams.items():
    print(group)