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
    for cycle, command in enumerate([command for line in open('inputDay10.txt', 'r') for command in line.split()]):
        if cycle in [19, 59, 99, 139, 179, 219]:
            pass
    return '-1'
