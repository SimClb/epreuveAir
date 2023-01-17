import OurLib
import colors 
import os 
import sys
# meta exercice 

# function 

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def metaTry():

    # prequisite

    files = []
    arg = []

    # take the name of files
    for i in range(13):
        nums= f'{i:02}'
        files.append(f'epAir{nums}.py')

    # take our arg in the txt file 
    f = open('arguments.txt', 'r')
    lines = f.readlines()

    for i in lines:
        arg.append(i.replace('\n', ''))

    f.close()
    # let's start our files 

    for (i, j) in zip(files, arg):
        try:
            blockPrint()
            print(os.system(f'python3 {i} {j}'))
            enablePrint()
            print(colors.bcolors.OKGREEN, f"{i}: success", colors.bcolors.ENDC)
        except ValueError:
            print(colors.bcolors.FAIL, f"{i} : failure", colors.bcolors.ENDC)


metaTry()

# finished 

