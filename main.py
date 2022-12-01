def elfHighesCarrCals():
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
    return calPerElf[-1] + calPerElf[-2] + calPerElf[-3]

if __name__ == '__main__':
    print(elfHighesCarrCals())