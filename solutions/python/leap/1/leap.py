def leap_year(year):
    four = year % 4 == 0
    hundred = year % 100 == 0
    fourhundred = year % 400 == 0

    return (four and hundred and fourhundred) or (four and not hundred)