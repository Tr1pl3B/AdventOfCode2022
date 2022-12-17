def GetSumOfSignalStrength() -> int:
    signalStrength = 0
    x = 1
    for cycle, command in enumerate([command for line in open('inputDay10.txt', 'r') for command in line.split()]):
        if cycle in [19, 59, 99, 139, 179, 219]:
            signalStrength = signalStrength + (cycle + 1) * x
        if command.isnumeric() or command[0] == '-':
            x += int(command)
    return signalStrength

def GetImmage() -> str:
    x = 1
    screen = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    for cycle, command in enumerate([command for line in open('inputDay10.txt', 'r') for command in line.split()]):
        row = int(cycle / 40)
        if cycle - 40 * row == x - 1:
            screen[row][cycle - 40 * row] = '#'
        elif cycle - 40 * row == x:
            screen[row][cycle - 40 * row] = '#'
        elif cycle - 40 * row == x + 1:
            screen[row][cycle - 40 * row] = '#'
        if command.isnumeric() or command[0] == '-':
            x += int(command)
    output = ''
    for row in screen:
        line = ''
        for char in row:
            line = line + char
        output = output + line + '\n'

    return output
