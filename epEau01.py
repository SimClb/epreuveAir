import sys 
import OurLib
import colors


# functions 

def splitByArg(list, separator):

    counter = 0
    start = [0]
    finish = [OurLib.lenCounter(list)]
    groups = []
    # put the finish balise in finish list
    for i in list: 
        if i == str(separator):
            finish.append(counter)
            start.append(counter + 1)
        counter += 1
    
    if counter == 0:
        print('error.')
        exit()

    # sort the finish list
    newFinish = OurLib.bubbleSort(finish)
    newStart = OurLib.bubbleSort(start)

    # put the groups
    objects = ""
    for (i,j) in zip(newStart, newFinish):
        for g in list[i:j]:
            objects += (str(g) +  " ")
        groups.append(objects)
        objects = ""

    return groups
        
# error management

if OurLib.lenCounter(sys.argv) != 3:
    print('error.')
    exit()

# exe 

for i in splitByArg(OurLib.splitFunction(sys.argv[1]), sys.argv[2]):
    print(i)


# finished 