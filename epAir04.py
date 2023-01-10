import sys 
import OurLib
import colors
# un seul à la fois 

# function 

def oneByOne(chars):

    list = []
    finishChars = ''

    for i in chars:
        list.append(i)

    restart = True # for the restart loop

    while restart:
        counter = 1

        for (i, j) in zip(list, list[1:]):
            restart = False
            if i == j: 
                del list[counter] # use del because remove del the first object who is same
                restart = True
                break # force restart 


            counter += 1 # for the index 

    for i in list:
        finishChars += i

    return finishChars

# error management 

if OurLib.lenCounter(sys.argv) != 2:
    print('error.')
    exit()


# exe

print(oneByOne(sys.argv[1]))

# finished 