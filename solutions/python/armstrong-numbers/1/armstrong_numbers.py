def is_armstrong_number(number):
    num_list = list(str(number))
    exponent = len(num_list)
    total = 0

    for digit in num_list:
        total += int(digit) ** exponent

    return total == number
        
    
