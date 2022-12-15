def elfHighesCarrCals(whichOne) -> int:
    calIn = open('inputDay1.txt', 'r')
    cals = 0
    calPerElf = list()
    for line in calIn:
        if line == '\n':
            calPerElf.append(cals)
            cals = 0
        else:
            cals += int(line)
    calPerElf.sort()
    return int(calPerElf[whichOne])