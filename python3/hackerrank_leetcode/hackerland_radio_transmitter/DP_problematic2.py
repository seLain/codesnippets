import sys
from collections import namedtuple, defaultdict

memory = defaultdict(int)

def hackerlandRadioTransmitters(x, k):
    x.sort()
    return recur_find_minimum(x, k, 0, len(x)-1)
        
def recur_find_minimum(x, k, left, right):
    
    n = right - left
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    
    if (left, right) in memory.keys():
        return memory[(left, right)]
    
    possible_minimum = []
    for i in range(left, right+1):
        left_bound = left
        right_bound = right
        #print('i:'+str(i)+' lb:'+str(left_bound)+' rb:'+str(right_bound))
        while x[i] - x[left_bound] > k:
            left_bound += 1
        while x[right_bound] - x[i] > k:
            right_bound -= 1
        #print('i2:'+str(i)+' lb:'+str(left_bound)+' rb:'+str(right_bound))
        left_minimum = recur_find_minimum(x, k, left, left_bound-1) if left_bound != i else 0
        right_minimum = recur_find_minimum(x, k, right_bound+1, right) if right_bound != i else 0
        possible_minimum.append(left_minimum+1+right_minimum)
        #print('possible_minimum:'+str(possible_minimum))
    minimum = min(possible_minimum)
    #print('minimum:'+str(minimum)+' returned.')
    memory[(left, right)] = minimum
    return memory[(left, right)]
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)