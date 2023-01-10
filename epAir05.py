import sys 
import OurLib
import colors
# sur chacun d'entre eux 

x = OurLib.lenCounter(sys.argv)
sign = sys.argv[x-1][0]
ope = sys.argv[x-1][1:]


# function 

def arithmeticer(list, signOpe, opeNumber):

    opeFinished = []

    if signOpe == '+':
        for i in list:
            opeFinished.append(int(i) + int(opeNumber))
    elif signOpe == '-':
        for i in list:
            opeFinished.append(int(i) - int(opeNumber))
    
    for i in opeFinished:
        print(i, end=' ')

# error management 

if x < 3:
    print('error.')
    exit()
for i in sys.argv[1:]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

if sign[0] != '-' and sign[0] != '+':
    print('error.')
    exit()

# exe 

arithmeticer(sys.argv[1:x-1], sign, ope)

# finished 