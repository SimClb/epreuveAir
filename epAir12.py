import sys
import OurLib
# quicksort 

# function 

def quicksort(array):
	if len(array) <= 1:
		return array
	pivot = array[len(array) // 2]
	left = [x for x in array if x < pivot]
	middle = [x for x in array if x == pivot]
	right = [x for x in array if x > pivot]

	return quicksort(left) + middle + quicksort(right)

# error managemnt 

for i in sys.argv[1:]:
	if not OurLib.isNumericHomeMade(i):
		print('error.')
		exit()

# exe 

print(quicksort(sys.argv[1:]))

# finished 