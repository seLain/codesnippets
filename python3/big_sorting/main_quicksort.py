import sys

def bigSorting(arr):
    # Complete this function
    if len(arr) < 2:
    	return arr
    quicksort(arr, 0, len(arr)-1)
    return arr

def quicksort(arr, low_idx, high_idx):
	if low_idx < high_idx:
		flag = partition(arr, low_idx, high_idx)
		quicksort(arr, low_idx, flag-1)
		quicksort(arr, flag+1, high_idx)
	return

def partition(arr, low_idx, high_idx):
	pivot_idx = pivot_index(low_idx, high_idx)
	# swap pivot to the last element
	arr[pivot_idx], arr[high_idx] = arr[high_idx], arr[pivot_idx]
	pivot = arr[high_idx]
	i = low_idx - 1
	for j in range(low_idx, high_idx):
		if compare(arr[j], pivot) == -1:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	# swap back
	arr[i+1], arr[high_idx] = arr[high_idx], arr[i+1]
	return i+1

def pivot_index(low_idx, high_idx):
	return (low_idx+high_idx)//2

def compare(str_val, base_val):

	if str_val == base_val:
		return 0

	# compare length first
	if len(str_val) > len(base_val):
		return 1
	elif len(str_val) < len(base_val):
		return -1
	else: # same length, compare by higher digits one by one
		for i in range(0, len(str_val)):
			if str_val[i] > base_val[i]:
				return 1
			elif str_val[i] < base_val[i]:
				return -1
			else:
				continue
