'''
Hackerrank: https://www.hackerrank.com/challenges/coin-change/problem
this solution will get timeout in many test cases
however, this solution can get all the combination during computation
'''
import sys

from collections import Counter, defaultdict
sys.setrecursionlimit(10000)

memory = defaultdict(list)

def recur_getWays(n, c):
    #print('enter: n='+str(n))
    if n < 0:
        return False, []
    elif n == 0:
        return True, [Counter()]
    
    if n in memory.keys():
        return True, memory[n]
    
    all_combs_count = []
    for coin in c:
        #print('choose coin:'+str(coin))
        valid, combs = recur_getWays(n-coin, c)
        if valid:
            for comb in combs:
                comb = comb + Counter({coin:1})
                existed = False
                for existed_comb in all_combs_count:
                    if existed_comb == comb:
                        existed = True
                        break
                if not existed:
                    all_combs_count.append(comb)
    #print('memorize: n='+str(n)+' count:'+str(all_combs_count))
    memory[n] = all_combs_count
    
    return True, all_combs_count

def getWays(n, c):
    # Complete this function
    valid, combs = recur_getWays(n, c)
    #print(memory)
    return len(combs)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)