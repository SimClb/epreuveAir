import sys
import OurLib
import colors
# chercher l'intru


# functions 

def findInterloper(list):

    notDouble = []

    for i in list:
        if not i in notDouble:
            notDouble.append(i)
        elif i in notDouble:
            notDouble.remove(i)


    strCounter = 0
    intCounter = 0 

    for i in notDouble:
        if OurLib.isNumericHomeMade(i):
            intCounter += 1
            print("+1 to intcounter", i)
        else:
            strCounter += 1
            print("+1 to strcounter", i)

    if intCounter > strCounter:
        for i in notDouble:
            if type(i) == str:
                notDouble.remove(i)
    elif strCounter > intCounter:
        for i in notDouble:
            if type(i) == int:
                notDouble.remove(i)

    if OurLib.lenCounter(notDouble) == 0:
        print('There are no object in this list...')
    elif OurLib.lenCounter(notDouble) > 0:
        for i in notDouble:
            print(i, end=' ')     

    print(strCounter, intCounter)

# error management 

if OurLib.lenCounter(sys.argv) < 3:
    print('error.')
    exit()

# exe 

findInterloper(sys.argv[1:])


# finished 