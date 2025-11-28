CHECK_CHAR = 'X'
ISBN_LENGTH = 10

def is_valid(isbn):
    digits = isbn.replace('-', '')[::-1]
    digit_length = len(digits)
    sum = 0
    
    if digit_length !=ISBN_LENGTH or not digits[1:].isnumeric():
        return False

    if not digits[0].isnumeric() and digits[0] != CHECK_CHAR:
        return False

    for index, digit in enumerate(digits):
        if digit.isnumeric():
            sum += int(digit) * (index + 1)
        else:
            sum += 10 * (index + 1)
        
    return sum % 11 == 0