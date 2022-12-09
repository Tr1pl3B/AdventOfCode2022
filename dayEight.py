def GetInput() -> list(list()):
    return [list(map(int, list(row.strip()))) for row in open('inputDay8.txt', 'r')]
def GetVisibeTrees() -> int:
    input = GetInput()
    notVisTrees = 0
    for row in range(1, len(input)-1):
        for column in range(1, len(input[row])-1):
            tree = input[row][column]
            notVis = GetNotVis(row, column, tree, input)
            if notVis:
                notVisTrees += 1
    visTrees = (len(input) * len(input[0])) - notVisTrees
    return visTrees

def GetNotVis(row, column, tree, input) -> bool:
    notVis = False
    if NotVisInRow(row, column, tree, input) and NotVisInColumn(row, column, tree, input):
        notVis = True
    return notVis


def NotVisInRow(row, column, tree, input) -> bool:
    vis = False
    smallest = 9
    bigL = bigR = 0
    for index, elem in enumerate(input[row]):
        if elem < smallest:
            smallest = elem
        if elem > bigL and index < column:
            bigL = elem
        elif elem > bigR and index > column:
            bigR = elem
    if bigL >= tree and bigR >= tree or elem <= smallest:
        vis = True
    return vis
def NotVisInColumn(row, column, tree, input) -> bool:
    vis = False
    smallest = 9
    bigU = bigD = 0
    for index, elem in enumerate(input):
        elem = elem[column]
        if elem < smallest:
            smallest = elem
        if elem > bigU and index < row:
            bigU = elem
        elif elem > bigD and index > row:
            bigD = elem
    if bigU >= tree and bigD >= tree or elem <= smallest:
        vis = True
    return vis
