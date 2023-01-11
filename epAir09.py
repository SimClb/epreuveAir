import sys 
import OurLib
import colors
# rotation vers la gauche

# function 

def rotationFunction(list):

    newList = []

    for i in list[1:]:
        newList.append(i)
    
    newList.append(list[0])

    for i in newList:
        print(i, end=', ')

# error management 

if OurLib.lenCounter(sys.argv) < 3:
    print('error.')
    exit()

# exe 

rotationFunction(sys.argv[1:])

# finished 