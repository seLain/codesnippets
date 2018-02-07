#!/bin/python3

# Hackerrank roads and libraries
# https://www.hackerrank.com/challenges/torque-and-development/problem

# idea behind this solution is to visit graph using DFS

import sys
from collections import defaultdict

class Graph:
    
    def __init__(self, n, edges):
        self.graph = {x:[] for x in range(1, n+1)}
        for edge in edges:  # note: the edge is bi-directional
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.visited = [False for x in range(0, len(self.graph)+1)] # first element is useless
    
    def dfs_visit(self, node):
        num_visit = 0
        if self.visited[node] is False:
            self.visited[node] = True
            num_visit = 1
            for n in self.graph[node]:
                num_visit += self.dfs_visit(n)
        return num_visit

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Complete this function
    
    # if cost of road is greater than cost of lib
    # just build lib for each city
    if len(cities) == 0 or c_road >= c_lib:
        return c_lib * n
    # graph construction
    graph = Graph(n, cities)
    # DFS visit
    cost = 0
    for i in range(1, n+1):
        num_roads = graph.dfs_visit(i) - 1 # num_roads is always less than visited nodes by 1
        if num_roads != -1:
            cost += c_lib + c_road * num_roads
    return cost

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