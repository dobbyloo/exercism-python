from math import sqrt

def score(x, y):
    points = 0
    
    distance = sqrt(abs(x)**2 + abs(y)**2)

    if distance <= 1:
        points = 10
    elif distance <= 5:
        points = 5
    elif distance <= 10:
        points = 1
    
    return points