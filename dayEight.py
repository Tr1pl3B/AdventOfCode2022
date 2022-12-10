def GetInput() -> list(list()):
    return [list(map(int, row.strip())) for row in open('inputDay8.txt', 'r')]
def GetVisibeTrees() -> int:
    arr = GetInput()
    result = 0

    # Iterate over the array
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            # Check if the current tree is visible from the left
            visibleFromLeft = True
            for k in range(column):
                if arr[row][k] >= arr[row][column]:
                    visibleFromLeft = False
                    break

            # Check if the current tree is visible from the right
            visibleFromRight = True
            for k in range(column + 1, len(arr[0])):
                if arr[row][k] >= arr[row][column]:
                    visibleFromRight = False
                    break

            # Check if the current tree is visible from the top
            visibleFromTop = True
            for k in range(row):
                if arr[k][column] >= arr[row][column]:
                    visibleFromTop = False
                    break

            # Check if the current tree is visible from the bottom
            visibleFromBottom = True
            for k in range(row + 1, len(arr)):
                if arr[k][column] >= arr[row][column]:
                    visibleFromBottom = False
                    break

            # If the current tree is visible from any direction,
            # increment the result
            if visibleFromLeft or visibleFromRight or visibleFromTop or visibleFromBottom:
                result += 1

    # Return the result
    return result

def GetHighestScenicScore() -> int:
    arr = GetInput()

    # Keep track of the maximum scenic score
    maxScenicScore = 0

    # Iterate over the array
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            # Calculate the scenic score of the current tree
            scenicScore = 1

            # Calculate the scenic score of the current tree
            # looking up
            numTreesInView = 0
            for k in range(row - 1, -1, -1):
                if arr[k][column] >= arr[row][column]:
                    numTreesInView += 1
                    break
                else:
                    numTreesInView += 1
            scenicScore *= numTreesInView

            # Calculate the scenic score of the current tree
            # looking left
            numTreesInView = 0
            for k in range(column - 1, -1, -1):
                if arr[row][k] >= arr[row][column]:
                    numTreesInView += 1
                    break
                else:
                    numTreesInView += 1
            scenicScore *= numTreesInView

            # Calculate the scenic score of the current tree
            # looking right
            numTreesInView = 0
            for k in range(column + 1, len(arr[0])):
                if arr[row][k] >= arr[row][column]:
                    numTreesInView += 1
                    break
                else:
                    numTreesInView += 1
            scenicScore *= numTreesInView

            # Calculate the scenic score of the current tree
            # looking down
            numTreesInView = 0
            for k in range(row + 1, len(arr)):
                if arr[k][column] >= arr[row][column]:
                    numTreesInView += 1
                    break
                else:
                    numTreesInView += 1
            scenicScore *= numTreesInView

            # Update the maximum scenic score
            maxScenicScore = max(maxScenicScore, scenicScore)


    # Return the maximum scenic score
    return maxScenicScore
