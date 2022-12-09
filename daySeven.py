cwd = root = dict()
virtPath = list()

def GetInput():
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

def GetSumOfDirUnder100000(direct = root):
    GetInput()
    if type(direct) == int:
        return (direct, 0)
    sum = 0
    ans = 0
    for sub in direct.values():
        subSum, subAns = GetSumOfDirUnder100000(sub)
        sum += subSum
        ans += subAns
    if sum <= 100000:
        ans += sum
    return (sum, ans)

def size(dir=root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))
def GetSizeDirToDelete():
    t = size() - 40_000_000
    def solve(dir=root):
        ans = float("inf")
        if size(dir) >= t:
            ans = size(dir)
        for child in dir.values():
            if type(child) == int:
                continue
            q = solve(child)
            ans = min(ans, q)
        return ans

    return solve()