def ticTaccToeOne() -> int:
    tttIn = open('inputDay2.txt', 'r')
    score = 0
    for line in tttIn:
        line = line.split()
        if line[1] == 'X':
            score += 1
            if line[0] == 'C':
                score += 6
            elif line[0] == 'A':
                score += 3

        elif line[1] == 'Y':
            score += 2
            if line[0] == 'A':
                score += 6
            elif line[0] == 'B':
                score += 3

        elif line[1] == 'Z':
            score += 3
            if line[0] == 'B':
                score += 6
            elif line[0] == 'C':
                score += 3

    return score

def ticTacToeTwo() -> int:
    tttIn = open('inputDay2.txt', 'r')
    score = 0
    for line in tttIn:
        line = line.split()
        if line[0] == 'A':
            if line[1] == 'X':
                score += 3 + 0
            elif line[1] == 'Y':
                score += 1 + 3
            else:
                score += 2 + 6

        elif line[0] == 'B':
            if line[1] == 'X':
                score += 1 + 0
            elif line[1] == 'Y':
                score += 2 + 3
            else:
                score += 3 + 6

        elif line[0] == 'C':
            if line[1] == 'X':
                score += 2 + 0
            elif line[1] == 'Y':
                score += 3 + 3
            else:
                score += 1 + 6

    return score