def is_isogram(string):
    lowercased = string.lower().replace('-', '').replace(' ', '')
    string_set = set(lowercased)
    string_list = list(lowercased)

    return len(string_list) == len(string_set)
    
