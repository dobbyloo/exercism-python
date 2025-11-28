def response(hey_bob):
    response = 'Whatever.'
    is_question = hey_bob.strip().endswith('?')
    is_upper = hey_bob.isupper()
    is_space = hey_bob.isspace()
    
    if is_question:
        response = 'Sure.'

    if is_upper:
        response = 'Whoa, chill out!'

    if is_question and is_upper:
        response = 'Calm down, I know what I\'m doing!'

    if is_space or len(hey_bob) == 0:
        response = 'Fine. Be that way!'

    return response
