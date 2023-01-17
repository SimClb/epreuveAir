import sys 
import OurLib
import colors 
# pyramid 

# function 

def pyramid(floor, char):

    for i in range(int(floor)):
        for j in range(int(floor) - i):
            print(' ', end='')

        print(char * (i + 1) + char * i)

# error management 

if OurLib.lenCounter(sys.argv) != 3:
    print('error. f')
    exit()

if not OurLib.isNumericHomeMade(sys.argv[1]):
    print('error. i')
    exit()

if OurLib.isNumericHomeMade(sys.argv[2]):
    print('error. k')
    exit()

# exe 

pyramid(sys.argv[1], sys.argv[2])

# finished