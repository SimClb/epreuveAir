import sys 
import OurLib
import colors
# afficher le contenu 

# function 

def shower(file):

    print(file.read())

    file.close()    

# error management 

if OurLib.lenCounter(sys.argv) != 2:
    print('error.')
    exit()

# check if we have a .txt file in arguements 
if sys.argv[1][OurLib.lenCounter(sys.argv[1]) - 4:] != '.txt':
    print('error.')
    exit()

# check if the file exists
try: 
    f = open(sys.argv[1], 'r')
except: 
    print('error. file not found')
    exit()

# exe

shower(f)

# finished 