import sys

from collections import defaultdict

class Node:
    def __init__(self, id):
        self.id = id
        self.status = 0 # 0 for peace, 1 for war
        self.sibling = set()
        self.owner = 0 # 0 for A, 1 for B
    def add_sibling(self, node):
        self.sibling.add(node)

class Graph:
    def __init__(self, n):
        self.nodes = [None] # let index 0 = None for easier code reading
        for i in range(1, n+1):
            self.nodes.append(Node(i))
    def set_owner(self, ownership_str):
        for i in range(1, len(ownership_str)+1):
            self.nodes[i].owner = int(ownership_str[i-1])
    def add_edge(self, edge):
        # build edge
        node_1 = self.nodes[edge[0]]
        node_2 = self.nodes[edge[1]]
        node_1.add_sibling(node_2)
        node_2.add_sibling(node_1)
        # check node status and update
        if node_1.owner == node_2.owner:
            node_1.status = 0
            node_2.status = 0
        else:
            if len(node_1.sibling) == 1:
                node_1.status = 1
            if len(node_2.sibling) == 1:
                node_2.status = 1
    def all_piece(self):
        for i in range(1, len(self.nodes)):
            if self.nodes[i].status == 1:
                return False
        return True

def kingdomDivision(n, roads):
    # Complete this function
    # all possible situations
    peace_counter = 0
    for i in range(0, pow(2,n)):
        str_i = ''.join(list(reversed(bin(i)[2:])))
        ## init the graph
        graph = Graph(n)
        graph.set_owner(str_i)
        for r in roads:
            graph.add_edge(r)
        ## check if all nodes are piece, if yes, add up the counter
        if graph.all_piece():
            peace_counter += 1
    return peace_counter

if __name__ == "__main__":
    n = int(input().strip())
    roads = []
    for roads_i in range(n-1):
       roads_t = [int(roads_temp) for roads_temp in input().strip().split(' ')]
       roads.append(roads_t)
    result = kingdomDivision(n, roads)
    print(result)