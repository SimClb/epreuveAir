import sys 
import OurLib
import colors 
# Mélanger deux tableaux triés ou non d'ailleurs 

index = 0

# funciton 

def blenderList(list):

    list1 = list[:index]
    list2 = list[index + 1:]
    listFusion = []

    for i in list1:
        listFusion.append(int(i))
    
    for j in list2:
        listFusion.append(int(j))

    for i in OurLib.bubbleSort(listFusion):
        print(i, end=' ')

# error management 

counter = 0 

if OurLib.lenCounter(sys.argv[1:]) < 4:
    print('error.')
    exit()

# check if the word fusion is well in the list + find his position 
for i in sys.argv[1:]:
    if i == 'fusion': 
        index += counter

    counter += 1


# if index = 0 ==> fusion is not in the list -> error
if index == 0:
    print('error.')
    exit()

# check if all the object in the list1 are numeric 
for i in sys.argv[1:index]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# check if all the object in the list2 are numeric 
for i in sys.argv[index + 2:]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# exe 

blenderList(sys.argv[1:])

# finished 