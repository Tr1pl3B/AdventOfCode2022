def getUselesAssignments() -> int():
    doubles = 0
    for line in open('inputDay4.txt', 'r'):
        a, b, x, y = map(int, line.replace(',', '-').split('-'))
        if a <= x and b >= y or x <= a and y >= b:
             doubles += 1
    return doubles

def getPairsOfOverlap() -> int():
    doubles = 0
    for line in open('inputDay4.txt', 'r'):
        a, b, x, y = map(int, line.replace(',', '-').split('-'))
        abRange = range(a,b+1)
        xyRange = range(x,y+1)
        for numb in abRange:
            if numb in xyRange:
                doubles += 1
                break
    return doubles
