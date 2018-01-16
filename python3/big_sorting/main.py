import sys

def bigSorting(arr):
    # Complete this function
    if len(arr) < 2:
    	return arr
    arr.sort(key=int)
    return arr
