import sys 
import OurLib
import colors
# contrôle de pass sanitaires


# function

def passSani(list):

    names = list[:OurLib.lenCounter(list) - 1]
    blockChar = list[OurLib.lenCounter(list) -1]
    okName = []

    for i in names:
        counter = 0
        for j in i:
            if j.lower() == blockChar.lower():
                counter += 1
        if counter == 0:
            okName.append(i)

    if okName:
        for i in okName:
            print(i, end=', ')
    else:
        print('Nobody allowed') 


# error management 

if OurLib.lenCounter(sys.argv) < 3:
    print('error.')
    exit()

for i in sys.argv[1:]: 
    if OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# exe 

passSani(sys.argv[1:])

# finished 