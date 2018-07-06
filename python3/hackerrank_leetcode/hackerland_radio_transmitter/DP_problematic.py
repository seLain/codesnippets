import sys
from collections import defaultdict

memory = defaultdict(int)

def hackerlandRadioTransmitters(x, k):
    # Complete this function
    x.sort()
    return recur_find_minimum(x, k, 0, len(x)-1)

def recur_find_minimum(x, k, left, right):
    
    if right - left < 2:
        return right - left
    if (left, right) in memory.keys():
        return memory[(left, right)]
    all_counts = []
    for i in range(left, right+1):
        left_outer = left - 1
        right_outer = right + 1
        for j in range(i, left-1, -1):
            if x[i] - x[j] > k:
                left_outer = j
                break
        for j in range(i, right+1, 1):
            if x[j] - x[i] <= k:
                right_outer = j+1
                break
        if (left, left_outer) not in memory.keys():
            if left <= left_outer:
                memory[(left, left_outer)] = recur_find_minimum(x, k, left, left_outer)
            else:
                memory[(left, left_outer)] = 0
        if (right_outer, right) not in memory.keys():
            if right_outer <= right:
                memory[(right_outer, right)] = recur_find_minimum(x, k, right_outer, right)
            else:
                memory[(right_outer, right)] = 0
        all_counts.append(memory[(left, left_outer)] + 1 + memory[(right_outer, right)])
    memory[(left, right)] = min(all_counts)
    return memory[(left, right)]
    

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)