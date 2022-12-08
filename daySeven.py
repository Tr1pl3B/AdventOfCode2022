from pathlib import Path
def getSumBigestDirs() -> int:
    dick = {'/': 0}
    cwd = list()

    for line in open('inputDay7.txt', 'r'):
        line = line.strip()
        if line[0] == '$':
            if line[2] == 'c':
                command, dir = line.replace('$', '').split()
                if dir == '/':
                    cwd = [dir]
                elif dir == '..':
                    cwd.pop()
                    if dir in dick.values():
                        dick[cwd[-1]] = dick[cwd[-1]]
                    else:
                        dick[cwd[-1]] = 0
                else:
                    cwd.append(dir)
            elif line[2] == 'l':
                pass
        else:
            first, second = line.split()
            if first[0].isdigit():
                dick[cwd[-1]] += int(first)

    for size in dick.values():
        if size > 100000:
            sum += size
    return sum
