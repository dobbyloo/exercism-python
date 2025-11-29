LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    if key > 26:
        key = key % 26
    
    cipher = LETTERS[key:] + LETTERS[:key]
    translation = str.maketrans(LETTERS + LETTERS.upper(), cipher + cipher.upper())
    return text.translate(translation)