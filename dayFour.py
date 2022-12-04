def getUselesAssignments() -> int():
    doubles = 0
    for line in open('inputDay4.txt', 'r'):
        a, b, x, y = map(int, line.replace(',', '-').split('-'))
        if a <= x and b >= y or x <= a and y >= b:
             doubles += 1
    return doubles

