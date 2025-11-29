def check_sides(sides):
    c = sides[0] + sides[1] > sides[2]
    a = sides[1] + sides[2] > sides[0]
    b = sides[0] + sides[2] > sides[1]

    return c and a and b

def equilateral(sides):
    s = set(sides)

    if 0 in s:
        return False

    return len(s) < 2 

def isosceles(sides):
    s = set(sides)
    
    if not check_sides(sides):
        return False

    return len(s) < 3

def scalene(sides):
    s = set(sides)

    if not check_sides(sides):
        return False

    return len(s) == 3
