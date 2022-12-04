import dayOne
import dayThree
import dayTwo

def breakLine(len) -> str:
    line = ''
    for x in range(len):
        line += '-'
    return line

if __name__ == '__main__':

    print('Day 1:')
    print('The elfe with the most cal\'s is carrying: ' + str(dayOne.elfHighesCarrCals(-1)))
    print('The top three elfe\'s are carrying: ' + str(dayOne.elfHighesCarrCals(-1) + dayOne.elfHighesCarrCals(-2) + dayOne.elfHighesCarrCals(-3)))
    print(breakLine(50))
    print('Day 2:')
    print('The totle score would be: ' + str(dayTwo.ticTaccToeOne()))
    print('With the right encoding the total score would be: ' + str(dayTwo.ticTacToeTwo()))
    print(breakLine(50))
    print('Day 3:')
    print('The sum of the priorities of the items are: ' + str(dayThree.getSumOfItemPrio()))
    print('The sum of the group batch priorities is: ' + str(dayThree.getSumOfGroupBatches()))