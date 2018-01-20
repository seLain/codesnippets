import sys, copy
from collections import defaultdict, Counter
sys.setrecursionlimit(10000)

memory = defaultdict(list)
memory[1] = [{1}]

def recur_powerSum(X, N):
    #print('enter f(x='+str(X)+')')
    if X == 1:
        return memory[1]
    
    all_combs = [] # keep all possible combinations as set instances
    k = 1
    next_X = X - pow(k, N)
    while next_X > 0:
        #print('prepare for enter f(x='+str(next_X)+') from f(x='+str(X)+')')
        if next_X not in memory.keys():
            remain_combs = recur_powerSum(next_X, N)
            memory[next_X] = remain_combs # keep in memory
        #print('end of f(x='+str(next_X)+') with '+str(len(memory[next_X]))+' combs. re-entering f(x='+str(X)+')')
        #print('combs:'+str(memory[next_X]))
        for comb in memory[next_X]:
            if k not in comb:
                new_comb = comb | {k}
                if new_comb not in all_combs:
                    all_combs.append(new_comb)
        #print('appended combs:'+str(all_combs))
        k += 1
        next_X = X - pow(k, N)
        #print('X:'+str(X)+' next:'+str(next_X))
        if next_X == 0:
            all_combs.append({k})
            break
        
    return all_combs

def powerSum(X, N):
    # Complete this function
    r = len(recur_powerSum(X, N))
    #print(memory)
    return r

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)