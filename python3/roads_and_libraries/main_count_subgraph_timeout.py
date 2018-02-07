#!/bin/python3

# Hackerrank roads and libraries
# https://www.hackerrank.com/challenges/torque-and-development/problem

# idea behind this solution is to count subgraphs (each subgraph needs only one library)
# and recovered roads

# this solution works with bad performance
# causes timeout in many test cases

import sys
from itertools import combinations

def count_subgraphs(n, comb_roads):
    cities = [x for x in range(1, n+1)]
    sub_graphs = []
    for r in comb_roads:
        [cities.remove(x) for x in r if x in cities]
        new_sg = True
        for sg in sub_graphs:
            if r[0] in sg or r[1] in sg:
                sg.update(set(r))
                new_sg = False
                break
        if new_sg:
            sub_graphs.append(set(r))
    return len(sub_graphs) + len(cities)

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Complete this function
    minimum_cost = n * c_lib + len(cities) * c_road
    for i in range(0, len(cities)+1):
        # using itertools.combinations to get all possible combinaitons of repaired roads
        iter_combs = combinations(cities, i)
        comb_roads = next(iter_combs, None)
        while comb_roads != None:
            # calculate the road cost
            cost_roads = len(comb_roads) * c_road
            # if the road cost already exceeds minimum_cost, continue the next iteration
            if cost_roads >= minimum_cost:
                comb_roads = next(iter_combs, None)
                continue
            # count the number of subgraphs
            num_subgraphs = count_subgraphs(n, comb_roads)
            cost_libs = num_subgraphs * c_lib
            # compare the total cost with known minimum cost
            if cost_roads + cost_libs < minimum_cost:
                minimum_cost = cost_roads + cost_libs
            # next iteration
            comb_roads = next(iter_combs, None)
            
    return minimum_cost

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
           cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)