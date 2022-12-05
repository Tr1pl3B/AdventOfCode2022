import re

def getInput() -> list(list()):
    cratesPre = list(list())
    instruction = list(list())
    stackCount = list()
    for line in open('inputDay5.txt', 'r'):
        if line[0] == '[':
            spaceCount = 0
            layer = list()
            for elem in line:
                if elem == ' ':
                    spaceCount += 1
                elif re.match('[A-Z]', elem):
                    if spaceCount > 1:
                        spaceCount /= 4
                        for i in range(int(spaceCount)):
                            layer.append('')
                            spaceCount = 0
                    layer.append(elem)
            cratesPre.append(layer)
        elif line[0] == ' ':
            stackCount = line.split()
        elif line[0] == 'm':
            instruction.append([int(numb) for numb in line.replace('move ', '').replace('from ', '').replace('to ', '').split()])

    stacks = list(list())
    for stack in range(len(stackCount)):
        stacks.append(list())
    for line in cratesPre:
        pos = 0
        for elem in line:
            if elem != '':
                stacks[pos].append(elem)
            pos += 1
    for stack in stacks:
        stack.reverse()
    return stacks, instruction

def getTopCrates9000() -> str:
    stacks, instruction = getInput()
    for line in instruction:
        count, fr, to = map(int, line)
        fr -= 1
        to -= 1
        for i in range(count):
            stacks[to].append(stacks[fr][len(stacks[fr])-1])
            stacks[fr].pop()
    out = ''
    for tower in stacks:
        out += str(tower[-1])
    return out

def getTopCrates9001() -> str:
    stacks, instruction = getInput()
    for line in instruction:
        count, fr, to = map(int, line)
        fr -= 1
        to -= 1
        frLen = len(stacks[fr])
        stacks[to].extend(stacks[fr][frLen - 1 - count:])
        for i in range(count - 1):
            stacks[fr].pop()
    out = ''
    for tower in stacks:
        out += str(tower[-1])
    return out