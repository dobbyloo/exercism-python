def translate(text):
    words = text.split(' ')
    translation = ''

    for word in words:
        translation += translate_word(word) + ' '

    return translation.rstrip()
    
def translate_word(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if text.startswith(vowels + ('xr', 'yt')):
        return text + 'ay'

    if text.startswith('y'):
        return text[1:] + text[0] + 'ay'

    if text.startswith('qu'):
        return text[2:] + 'quay'
    elif text[1:].startswith('qu'):
        return text[3:] + text[0] + 'quay'

    for index, char in enumerate(text):            
        if char in str(vowels) or char == 'y':
            prefix = text[0:index]
            root = text[index:]
            return root + prefix + 'ay'