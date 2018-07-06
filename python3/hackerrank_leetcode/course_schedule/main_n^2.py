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
            dict_edges = {c[0]:c[1] for c in prerequisites}
            for edge in prerequisites:
                passed_courses = [edge[0]]
                current_c = edge[0]
                next_c = edge[1]
                while next_c in dict_edges.keys():
                    current_c = next_c
                    next_c = dict_edges[current_c]
                    if next_c in passed_courses:
                        return False
                    else:
                        passed_courses.append(current_c)
            return True
