from collections import defaultdict
 
class Graph():
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
        self.num_of_vertices = num_of_vertices
 
    def addEdge(self, src_node, dest_node):
        self.graph[src_node].append(dest_node)
 
    def isCyclicUtil(self, cur_node_idx, visited, dpf_stack):
 
        # mark current node as visited
        visited[cur_node_idx] = True
        # recording to the depth-first stack trace
        dpf_stack[cur_node_idx] = True
 
        # visit all neighbours recursively
        # if any neighbor is already visited and 
        # also found in dpf_stack then graph is cyclic
        for neighbor in self.graph[cur_node_idx]:
            if visited[neighbor] == False:	# visit this neighbor
                if self.isCyclicUtil(neighbor, visited, dpf_stack) == True:
                    return True
            elif dpf_stack[neighbor] == True: # it is possible the neighbor visited
                return True                    # in previous recursion, but no cycle found
 
        # recovering the depth-first stack trace before this step ends
        dpf_stack[cur_node_idx] = False

        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.num_of_vertices
        dpf_stack = [False] * self.num_of_vertices	# depth first stack
        for node_idx in range(self.num_of_vertices):
            if visited[node_idx] == False:
                if self.isCyclicUtil(node_idx, visited, dpf_stack) == True:
                    return True
        return False

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2:
            return True
        else:
        	graph = Graph(numCourses)
        	for p in prerequisites:
        		graph.addEdge(p[0], p[1])
        	return not graph.isCyclic()


