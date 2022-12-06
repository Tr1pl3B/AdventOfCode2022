def getInput() -> str:
    return open('inputDay6.txt', 'r').read()

def getIndex(numbOfChars) -> int:
        input = list(getInput().strip())
        count = numbOfChars
        temp = input[:numbOfChars]
        for i in range(numbOfChars):
            input.pop(i)
        for char in input:
            if len(temp) != len(dict.fromkeys(temp)):
                temp.append(char)
                temp.pop(0)
                count += 1
            else:
                break
        return count