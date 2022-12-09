def GetInput() -> list(list()):
    return [list(map(int, row.strip())) for row in open('inputDay8.txt', 'r')]
def GetVisibeTrees() -> int:
    arr = GetInput()
    result = 0

    # Iterate over the array
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # Check if the current tree is visible from the left
            visible_from_left = True
            for k in range(j):
                if arr[i][k] >= arr[i][j]:
                    visible_from_left = False
                    break

            # Check if the current tree is visible from the right
            visible_from_right = True
            for k in range(j + 1, len(arr[0])):
                if arr[i][k] >= arr[i][j]:
                    visible_from_right = False
                    break

            # Check if the current tree is visible from the top
            visible_from_top = True
            for k in range(i):
                if arr[k][j] >= arr[i][j]:
                    visible_from_top = False
                    break

            # Check if the current tree is visible from the bottom
            visible_from_bottom = True
            for k in range(i + 1, len(arr)):
                if arr[k][j] >= arr[i][j]:
                    visible_from_bottom = False
                    break

            # If the current tree is visible from any direction,
            # increment the result
            if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
                result += 1

    # Return the result
    return result