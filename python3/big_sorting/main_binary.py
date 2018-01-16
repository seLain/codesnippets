import sys

def bigSorting(arr):
    # Complete this function
    if len(arr) < 2:
    	return arr

    sorted_arr = [arr[0]]
    for str_val in arr[1:]:
    	sorted_arr = binary_sort(sorted_arr, str_val)
    return sorted_arr

def binary_sort(sorted_arr, str_val):

	head_idx = 0
	tail_idx = len(sorted_arr)-1

	# compare with head first
	larger = compare(str_val, sorted_arr[head_idx])
	if larger <= 0:
		sorted_arr.insert(0, str_val)
		return sorted_arr

	# compare with tail
	larger = compare(str_val, sorted_arr[tail_idx])
	if larger >= 0:
		sorted_arr.insert(tail_idx+1, str_val)
		return sorted_arr

	base_idx = (head_idx+tail_idx)//2
	while True:
		# compare base str_value with str_val
		larger = compare(str_val, sorted_arr[base_idx])
		if larger == 1: # str_val > str_value
			head_idx = base_idx
			base_idx = (head_idx+tail_idx)//2
		elif larger == 0: # str_val = str_value
			sorted_arr.insert(base_idx, str_val)
			return sorted_arr
		else:
			tail_idx = base_idx
			base_idx = (head_idx+tail_idx)//2
		# ending condition : mallest interval
		if tail_idx - head_idx == 1:
			sorted_arr.insert(tail_idx, str_val)
			return sorted_arr

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
