import OurLib
import colors
import sys
# split exercise 


# functions 

def splitFunction(list):
  
    start = [0]
    finish = [OurLib.lenCounter(list)]
    words = []
    counter = 0

    # put the index of space in the list 
    for i in list:
        if str(i) == ' ':
            # we put the space index in the finish words list
            finish.append(counter)     

        counter += 1


        

    # let's sort the spaces tab 
    sorterFinish = OurLib.bubbleSort(finish)
    
    # let's append the start words
    for j in sorterFinish[0:(OurLib.lenCounter(sorterFinish) - 1)]:
        start.append(j + 1)

    # let's find the words from the start and finish
    for (i , j) in zip(start, sorterFinish):
        words.append(list[i:j])



    return words


# error management

if OurLib.lenCounter(sys.argv) != 2:
    print('error.')
    exit()

# exe 

tab = splitFunction(sys.argv[1])

for i in tab:
    print(i)


# finished 