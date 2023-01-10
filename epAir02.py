import sys 
import OurLib
import colors
# concat 

# functions 

def concat(list, separator):

    for i in list: 
        print(i, end=separator)




# error management 

if OurLib.lenCounter(sys.argv) < 3:
    print('error.')
    exit()

# exe 

s = (OurLib.lenCounter(sys.argv) -1)
f = (OurLib.lenCounter(sys.argv) -2)

concat(sys.argv[1:f], sys.argv[s])

# finished