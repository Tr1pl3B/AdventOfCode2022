from pathlib import Path

def GetSumSmallestDirs() -> int:
    folderSizes = dict()
    virtPath = Path('')
    sum = 0
    for line in open('inputDay7.txt', 'r'):
        line = line.strip()
        if line[0] == '$':
            if line[2] == 'c':
                command, direct = line.replace('$', '').strip().split()
                if direct == '..':
                    virtPath = virtPath.parent
                else:
                    virtPath = virtPath/ direct
        elif line[0] != 'd':
            size, file = line.split()
            direct = virtPath.name
            if direct in folderSizes.keys():
                folderSizes[direct] += int(size)
            else:
                folderSizes[direct] = int(size)
    print()
    # for line in open('inputDay7.txt', 'r'):
    #     line = line.strip()
    #     if line[0] == '$' and line[2] == 'c':
    #         command, direct = line.replace('$', '').strip().split()
    #         if direct == '..':
    #             virtPath = virtPath.parent
    #         else:
    #             virtPath = virtPath/direct
    #     elif line[0] == 'd':
    #
    #         folderSizes[]

