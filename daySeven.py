cwd = root = dict()
virtPath = list()
def GetSumSmallestDirs() -> int:
    for line in open('inputDay7.txt', 'r'):
        line = line.strip()
        if line[0] == '$':
            if line[2] == 'c':
                command, direct = line.replace('$', '').strip().split()
                if direct == '..':
                    cwd = virtPath.pop()
                elif direct == '/':
                    cwd = root
                    virtPath = list()
                else:
                    if direct not in cwd:
                        cwd[direct] = dict()
                    virtPath.append(cwd)
                    cwd = cwd[direct]
        else:
            first, second = line.split()
            if first == 'dir':
                if second not in cwd:
                    cwd[second] = dict()
            else:
                cwd[second] = int(first)
    return(GetIt()[1])

def GetIt(direct = root):
    if type(direct) == int:
        return (direct, 0)
    sum = 0
    ans = 0
    for sub in direct.values():
        subSum, subAns = GetIt(sub)
        sum += subSum
        ans += subAns
    if sum <= 100000:
        ans += sum
    return (sum, ans)

