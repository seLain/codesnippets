import itertools, copy

def calculate_unfair(li_list, lu_list):
    global memory, memory2, min_unfair
    unfair = 0
    for x in li_list:
        for y in lu_list:
            if frozenset({x, y}) not in memory2.keys():
                memory2[frozenset({x, y})] = abs(x-y)
            unfair += memory2[frozenset({x, y})]
            if min_unfair is not None and unfair > min_unfair:
                return
    memory[comb] = unfair
    if min_unfair is None:
        min_unfair = unfair
    elif min_unfair > unfair:
        min_unfair = unfair

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
arr = list(map(int, input().strip().split(' ')))

memory = {}
memory2 = {}
min_unfair = None
combs = itertools.combinations(arr, m)
comb = next(combs, None)
while comb:
    if comb not in memory.keys():
        li_list = comb
        lu_list = copy.copy(arr)
        for x in comb:
            lu_list.remove(x)
        calculate_unfair(li_list, lu_list)
    comb = next(combs, None)
        
print(min_unfair)