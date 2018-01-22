'''
Hackerrank: https://www.hackerrank.com/challenges/equal/problem

using solution mentioned in discussion area. 
reverse thinking: "dispatch chocolates" => "taken away chocolates" until 0 or equal
'''

import sys, copy
from collections import defaultdict

memory = defaultdict(int)
minimum_ops_count = None

def ops_to_base(start_val, base_val, dec_opts):
    diff = start_val - base_val
    if diff == 0:
        memory[(start_val, base_val)] = 0
        return 0
    else:
        counter = 0
        for m in dec_opts:
            times, diff = divmod(diff, m)
            counter += times
            if diff == 0:
                break
        memory[(start_val, base_val)] = counter
        return counter

def equal(arr):
    global minimum_ops_count
    minimum_ops_count = max(arr)*len(arr)
    min_val = min(arr)
    dec_opts = [1,2,5]
    dec_opts = sorted(dec_opts, reverse=True)
    for i in range(min_val, -1, -1):  # iterating the base from 0 to min(arr)
        local_count = 0
        for j in range(0, len(arr)):
            if (arr[j], i) not in memory.keys():
                local_count += ops_to_base(arr[j], i, dec_opts)
            else:
                local_count += memory[(arr[j], i)]
            # check if current local count already exceeds known minimum count
            # if yes, you can stop the computation now
            if local_count > minimum_ops_count:
                break
        # if local count in this iteration is maller than the known minimum,
        # apparently the minumum should be updated
        if local_count < minimum_ops_count:
            minimum_ops_count = local_count
    #print(all_ops_count)
    return minimum_ops_count

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = equal(arr)
        print(result)