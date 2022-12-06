def getInput() -> str:
    return open('inputDay6.txt', 'r').read()

def getIndex() -> int:
        orgIn = getInput()
        input = list(getInput().strip())
        count = 4
        temp = input[:4]
        for i in range(4):
            input.pop(i)
        for char in input:
            if len(temp) != len(dict.fromkeys(temp)):
                temp.append(char)
                temp.pop(0)
                count += 1
            else:
                break
        print()
        return count