import sys
import OurLib
import colors
# Insertion dans un tableau trié 

# function

def numberInsertion(list):

    sortedList = list[:OurLib.lenCounter(list) - 1]
    addNumber = list[OurLib.lenCounter(list) - 1]

    sortedList.append(addNumber)

    for i in OurLib.bubbleSort(sortedList):
        print(i, end=' ')

# error management 

if OurLib.lenCounter(sys.argv) < 3:
    print('error.')
    exit()

for i in sys.argv[1:]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# exe 

numberInsertion(sys.argv[1:])

# finished 