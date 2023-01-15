import sys
import OurLib
# quicksort 

# function 

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

# error managemnt 

for i in sys.argv[1:]:
	if not OurLib.isNumericHomeMade(i):
		print('error.')
		exit()

# exe 

print(quicksort(sys.argv[1:]))

# finished 