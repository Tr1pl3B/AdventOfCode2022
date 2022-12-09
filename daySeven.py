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
                    folderList = [folder for folder in virtPath.glob('**/*') if folder.is_dir()]
                    for folder in folderList:
                        folderSizes[folder] = folder.stat().st_size
                    virtPath = virtPath.parent
                else:
                    virtPath = virtPath/ direct
        else:
            size, file = line.split()
            direct = virtPath.name
            if direct in folderSizes.keys():
                folderSizes[direct] += int(size)
            else:
                folderSizes[direct] = int(size)
                
    return -1