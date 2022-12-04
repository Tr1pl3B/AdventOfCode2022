def getInputDayThree() -> list(list()):
    input = list(list())
    for line in open('inputDay3.txt', 'r'):
        values = list()
        for char in line:
            if char.islower():
                values.append(ord(char) - 96)
            elif char.isupper():
                values.append(ord(char) - 38)
        input.append(values)
    return input

def getSumOfItemPrio() -> int:
    input = getInputDayThree()
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

def getSumOfGroupBatches() -> int:
    input = getInputDayThree()
    groups = [input[index: index + 3] for index in range(0, len(input), 3)]
    count = 0
    for group in groups:
        for value in group[0]:
            if value in group[1] and value in group[2]:
                count += value
                break
    return count