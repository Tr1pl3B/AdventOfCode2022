import dayFive
import dayOne
import daySeven
import daySix
import dayThree
import dayTwo
import dayFour
from pathlib import Path

def breakLine(len) -> str:
    line = ''
    for x in range(len):
        line += '-'
    return line

if __name__ == '__main__':

    print('|' + breakLine(70))
    print('|Day 1:')
    print('|The elfe with the most cal\'s is carrying: ' + str(dayOne.elfHighesCarrCals(-1)))
    print('|The top three elfe\'s are carrying: ' + str(dayOne.elfHighesCarrCals(-1) + dayOne.elfHighesCarrCals(-2) + dayOne.elfHighesCarrCals(-3)))
    print('|' + breakLine(70))
    print('|Day 2:')
    print('|The totle score would be: ' + str(dayTwo.ticTaccToeOne()))
    print('|With the right encoding the total score would be: ' + str(dayTwo.ticTacToeTwo()))
    print('|' + breakLine(70))
    print('|Day 3:')
    print('|The sum of the priorities of the items are: ' + str(dayThree.getSumOfItemPrio()))
    print('|The sum of the group batch priorities is: ' + str(dayThree.getSumOfGroupBatches()))
    print('|' + breakLine(70))
    print('|Day 4:')
    print('|The sum of the pairs with fully contained assignments is: ' + str(dayFour.getUselesAssignments()))
    print('|The sum of overlapping pairs is: ' + str(dayFour.getPairsOfOverlap()))
    print('|' + breakLine(70))
    print('|Day 5')
    print('|The crates on Top, with crane 9000, are: ' + dayFive.getTopCrates9000())
    print('|The crates on Top, with crane 9001, are: ' + dayFive.getTopCrates9001())
    print('|' + breakLine(70))
    print('|Day 6')
    print('|Number of chars processed before first start-of-packet marker: ' + str(daySix.getIndex(4)))
    print('|Number of chars processed before first start-of-message marker: ' + str(daySix.getIndex(14)))
    print('|' + breakLine(70))
    print('|Day 7')
    print('|Sum of Dicts under 100000 in size is: ' + str(daySeven.GetSumOfDirUnder100000()[1]))
    print('|The Directory to delete has the size: ' + str(daySeven.GetSizeDirToDelete()))

