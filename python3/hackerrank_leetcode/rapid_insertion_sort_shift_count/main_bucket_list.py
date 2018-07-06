import sys

def insertionSort(arr):
    # Complete this function
    shift_count = 0
    largest = arr[0]
    dict_count = [0] * (max(set(arr)) + 1) # dict_count[0] is useless for easier code reading
    dict_count[arr[0]] += 1
    for i in range(1, len(arr)):
        if largest > arr[i]:
            shift_count += sum(dict_count[arr[i]+1:])
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