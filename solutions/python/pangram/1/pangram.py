import string

def is_pangram(sentence):
    lower_cased = sentence.lower()
    letters = list(string.ascii_lowercase)
    letters_found = dict.fromkeys(letters, False)

    for letter in letters:
        if lower_cased.find(letter) != -1:
            letters_found[letter] = True
            continue;

    return len([letter for letter in letters_found.values() if letter == True]) == 26