def GetInput() -> list(list()):
    return [[row.split()[0], int(row.split()[1])] for row in open('inputDay9.txt')]

def GetPosVisOnce() -> int:
    input = GetInput()
    grid = [['s']]
    headPos = [0, 0]
    tailPos = [0, 0]
    oldHead = list()
    for command in input:
        direction = command[0].upper()
        count = command[1]
        if direction == 'R':
            for index in range(count):
                oldHead = headPos[:]
                if len(grid[headPos[0]]) - 1 == headPos[1]:
                    grid[headPos[0]].append('.')
                headPos[1] += 1
                grid, tailPos = TailMovement(grid, headPos, tailPos, oldHead)
        if direction == 'D':
            for index in range(count):
                oldHead = headPos[:]
                if len(grid) - 1 == headPos[0]:
                    grid.append(['.'] * len(grid[headPos[0]]))
                headPos[0] += 1
                grid, tailPos = TailMovement(grid, headPos, tailPos, oldHead)
        if direction == 'L':
            for index in range(count):
                oldHead = [headPos[0], headPos[1]+1]
                if 0 == headPos[1]:
                    grid[headPos[0]].insert(0, '.')
                    grid[headPos[0]].append('.')
                tailPos[1] += 1
                grid, tailPos = TailMovement(grid, headPos, tailPos, oldHead)
        if direction == 'U':
            for index in range(count):
                oldHead = [headPos[0]+1, headPos[1]]
                if 0 == headPos[0]:
                    grid.insert(0, ['.'] * len(grid[headPos[0]]))
                    grid.append(['.'] * len(grid[headPos[0]]))
                tailPos[0] += 1
                grid, tailPos = TailMovement(grid, headPos, tailPos, oldHead)

    countPlaces = 0
    for row in grid:
        for column in row:
            countPlaces += 1
    return countPlaces

def TailMovement(grid, headPos, tailPos, oldHead) -> list(list()):
    if headPos[0] - tailPos[0] + headPos[1] - tailPos[1] not in [-1, 0, 1]:
        tailPos = oldHead
        grid[tailPos[0]][tailPos[1]] = '#'
    return grid, tailPos