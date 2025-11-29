LETTER_MAP = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 
    'f': 5, 'g': 6, 'h':7, 'i': 8, 
    'j': 9, 'k': 10, 'l': 11, 'm': 12,
    'n': 13, 'o': 14, 'p': 15, 'q': 16, 
    'r': 17, 's': 18, 't': 19, 'u':20, 
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
}

def rotate(text, key):
    cipher = list(LETTER_MAP.keys())
    translation = ""
    
    for char in text:
        lower = char.islower()
        
        if char.isalpha():
            if lower:
                index = LETTER_MAP[char] + key
            else:
                index = LETTER_MAP[char.lower()] + key

            if index > 25:
                index = index % 26
            
            translation += cipher[index] if lower else cipher[index].upper()

        else:
            translation += char

    return translation
        
    
