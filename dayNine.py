def GetInput() -> list(list()):
    return [[row.split()[0], int(row.split()[1])] for row in open('inputDay9.txt')]

