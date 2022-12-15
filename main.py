import day10
import day8
import day5
import day9
import day1
import day7
import day6
import day3
import day2
import day4
from pathlib import Path

def breakLine(len) -> str:
    line = ''
    for x in range(len):
        line += '-'
    return line

if __name__ == '__main__':

    print('|' + breakLine(70))
    print('|Day 1:')
    print('|The elfe with the most cal\'s is carrying: ' + str(day1.elfHighesCarrCals(-1)))
    print('|The top three elfe\'s are carrying: ' + str(day1.elfHighesCarrCals(-1) + day1.elfHighesCarrCals(-2) + day1.elfHighesCarrCals(-3)))
    print('|' + breakLine(70))
    print('|Day 2:')
    print('|The totle score would be: ' + str(day2.ticTaccToeOne()))
    print('|With the right encoding the total score would be: ' + str(day2.ticTacToeTwo()))
    print('|' + breakLine(70))
    print('|Day 3:')
    print('|The sum of the priorities of the items are: ' + str(day3.getSumOfItemPrio()))
    print('|The sum of the group batch priorities is: ' + str(day3.getSumOfGroupBatches()))
    print('|' + breakLine(70))
    print('|Day 4:')
    print('|The sum of the pairs with fully contained assignments is: ' + str(day4.getUselesAssignments()))
    print('|The sum of overlapping pairs is: ' + str(day4.getPairsOfOverlap()))
    print('|' + breakLine(70))
    print('|Day 5')
    print('|The crates on Top, with crane 9000, are: ' + day5.getTopCrates9000())
    print('|The crates on Top, with crane 9001, are: ' + day5.getTopCrates9001())
    print('|' + breakLine(70))
    print('|Day 6')
    print('|Number of chars processed before first start-of-packet marker: ' + str(day6.getIndex(4)))
    print('|Number of chars processed before first start-of-message marker: ' + str(day6.getIndex(14)))
    print('|' + breakLine(70))
    print('|Day 7')
    print('|Sum of Dicts under 100000 in size is: ' + str(day7.GetSumOfDirUnder100000()[1]))
    print('|The Directory to delete has the size: ' + str(day7.GetSizeDirToDelete()))
    print('|' + breakLine(70))
    print('|Day 8')
    print('|The number of visible trees is: ' + str(day8.GetVisibeTrees()))
    print('|The highes scenic score is: ' + str(day8.GetHighestScenicScore()))
    print('|' + breakLine(70))
    print('|Day 9')
    print('|The number of positions visited at least once by the tail: ' + str(day9.GetPosVisOnce()))
    print('|!Falsch!The number of pxositions visited at least once by the tail (10 Knot rope): ' + str(day9.GetPosVisOnce10Knots()))
    print('|Day 10')
    print('|The sum of the signal strength is: ' + str(day10.GetSumOfSignalStrength()))
    # print('|The highes scenic score is: ' + str(dayEight.GetHighestScenicScore()))
    # print('|' + breakLine(70))
