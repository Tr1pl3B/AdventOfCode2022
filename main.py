def elfHighesCarrCals(whichOne) -> int:
    calIn = open('inputCals.txt', 'r')
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

def ticTaccToeOne() -> int:
    tttIn = open('inputTTT.txt', 'r')
    score = 0
    for line in tttIn:
        line = line.split()
        if line[1] == 'X':
            score += 1
            if line[0] == 'C':
                score += 6
            elif line[0] == 'A':
                score += 3

        elif line[1] == 'Y':
            score += 2
            if line[0] == 'A':
                score += 6
            elif line[0] == 'B':
                score += 3

        elif line[1] == 'Z':
            score += 3
            if line[0] == 'B':
                score += 6
            elif line[0] == 'C':
                score += 3

    return score

def ticTacToeTwo() -> int:
    tttIn = open('inputTTT.txt', 'r')
    score = 0
    for line in tttIn:
        line = line.split()
        if line[0] == 'A':
            if line[1] == 'X':
                score += 3 + 0
            elif line[1] == 'Y':
                score += 1 + 3
            else:
                score += 2 + 6

        elif line[0] == 'B':
            if line[1] == 'X':
                score += 1 + 0
            elif line[1] == 'Y':
                score += 2 + 3
            else:
                score += 3 + 6

        elif line[0] == 'C':
            if line[1] == 'X':
                score += 2 + 0
            elif line[1] == 'Y':
                score += 3 + 3
            else:
                score += 1 + 6

    return score

def getSumOfItemPrio() -> int:
    input = list(list())
    for line in open('inputSOIP.txt', 'r'):
        values = list()
        for char in line:
            if char.islower():
                values.append(ord(char) - 96)
            elif char.isupper():
                values.append(ord(char) - 38)
        input.append(values)
    count = 0
    for bag in input:
        mid = int(len(bag) / 2)
        comp1 = bag[:mid]
        comp2 = bag[mid:]
        for comp in bag:
            for value in comp1:
                if value in comp2:
                    count += value
                    break
            break
    return count


def breakLine(len) -> str:
    line = ''
    for x in range(len):
        line += '-'
    return line

if __name__ == '__main__':

    print('Day 1:')
    print('The elfe with the most cal\'s is carrying: ' + str(elfHighesCarrCals(-1)))
    print('The top three elfe\'s are carrying: ' + str(elfHighesCarrCals(-1) + elfHighesCarrCals(-2) + elfHighesCarrCals(-3)))
    print(breakLine(50))
    print('Day 2:')
    print('The totle score would be: ' + str(ticTaccToeOne()))
    print('With the right encoding the total score would be: ' + str(ticTacToeTwo()))
    print('Day 3:')
    print('The sum of the priorities of the items are: ' + str(getSumOfItemPrio()))