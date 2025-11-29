"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 2
EQUAL = 1
UNEQUAL = -1

def equal_values(list_one, list_two):
    contains_equal = True

    for i in range(0, len(list_one)):
        if list_one[i] != list_two[i]:
            contains_equal = False
            break
    
    return (len(list_one) == 0 and len(list_two) == 0) or contains_equal

def has_subset(check_set, search_set, check_len = 1):
    for index, item in enumerate(search_set):
        for i in check_set:
            if i == item:
                chunk = search_set[index:index + check_len]
                if equal_values(check_set, chunk):
                    return True
    return False

def sublist(list_one, list_two):
    one_len = len(list_one)
    two_len = len(list_two)
 
    if (one_len < two_len and has_subset(list_one, list_two, one_len)) or (one_len == 0 and two_len != 0):
            return SUBLIST
    if (two_len < one_len and has_subset(list_two, list_one, two_len)) or (one_len !=0 and two_len == 0):
            return SUPERLIST
    if equal_values(list_one, list_two):
        return EQUAL
    else:
        return UNEQUAL
    