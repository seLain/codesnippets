import sys
from collections import defaultdict

def insertionSort(arr):
    # Complete this function
    shift_count = 0
    largest = arr[0]
    dict_count = defaultdict(int)
    dict_count[arr[0]] += 1
    for i in range(1, len(arr)):
        if largest > arr[i]:
            shift_count += sum([dict_count[k] for k in dict_count.keys() if k > arr[i]])
        else:
            largest = arr[i]
        dict_count[arr[i]] += 1
        
    return shift_count

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertionSort(arr)
        print(result)