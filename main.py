def elfHighesCarrCals(whichOne):
    puzIn = open('puzInput.txt', 'r')
    cals = 0
    calPerElf = list()
    for line in puzIn:
        if line == '\n':
            calPerElf.append(cals)
            cals = 0
        else:
            cals += int(line)
    calPerElf.sort()
    return int(calPerElf[whichOne])

def breakLine(len):
    line = ''
    for x in range(len):
        line += '-'
    return line

if __name__ == '__main__':

    print("Day 1:")
    print('The elfe with the most cal\'s is carrying: ' + str(elfHighesCarrCals(-1)))
    print('The top three elfe\'s are carrying: ' + str(elfHighesCarrCals(-1) + elfHighesCarrCals(-2) + elfHighesCarrCals(-3)))
    print(breakLine(50))