def GetInput() -> list(list()):
    return [[row.split()[0], int(row.split()[1])] for row in open('inputDay9.txt')]

def GetPosVisOnce() -> int:
    input = GetInput()
    grid = [['s']]
    headPos = [0, 0]
    tailPos = [0, 0]
    for command in input:
        direction = command[0].upper()
        count = command[1]
        for index in range(count):
            grid, tailPos = MoveHead(grid, headPos, tailPos, direction, True)
    return CountPlacesVis(grid)

def GetPosVisOnce10Knots() -> int:
    input = GetInput()
    grid = [['s']]
    knots = [[0, 0]] * 10
    for command in input:
        direction = command[0].upper()
        count = command[1]
        for index in range(count):
            for knot in range(len(knots) - 1):
                headPos = knots[knot][:]
                tailPos = knots[knot + 1][:]
                theOneTail = False
                if knot == len(knots) - 2:
                    theOneTail = True
                grid, tailPos = MoveHead(grid, headPos, tailPos, direction, theOneTail)
                knots[knot] = headPos[:]
                knots[knot + 1] = tailPos[:]
    return CountPlacesVis(grid)


def CountPlacesVis(grid) -> int:
    countPlaces = 0
    for row in grid:
        for column in row:
            if column in ['s', '#']:
                countPlaces += 1
    return countPlaces

def MoveHead(grid, headPos, tailPos, direction, theOneTail):
    oldHead = headPos[:]
    if direction == 'R':
        if len(grid[headPos[0]]) - 1 == headPos[1]:
            for line in grid:
                line.append('.')
        headPos[1] += 1
    elif direction == 'D':
        if len(grid) - 1 == headPos[0]:
            grid.append(['.'] * len(grid[headPos[0]]))
        headPos[0] += 1
    elif direction == 'L':
        if 0 == headPos[1]:
            for line in grid:
                line.insert(0, '.')
            oldHead[1] += 1
            tailPos[1] += 1
        else:
            headPos[1] -= 1
    elif direction == 'U':
        if 0 == headPos[0]:
            grid.insert(0, ['.'] * len(grid[headPos[0]]))
            oldHead[0] += 1
            tailPos[0] += 1
        else:
            headPos[0] -= 1
    return TailMovement(grid, headPos, tailPos, oldHead, theOneTail)

def TailMovement(grid, headPos, tailPos, oldHead, theOneTail) -> list(list()):
    dif = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]]
    if dif[0] not in [-1, 0, 1] or  dif[1] not in [-1, 0, 1]:
        tailPos = oldHead
        if theOneTail:
            grid[tailPos[0]][tailPos[1]] = '#'
    return grid, tailPos