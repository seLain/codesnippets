from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        if numCourses < 2:
            return True

        graph = defaultdict(list)
        num_of_depends = defaultdict(int)
        for s, e in set(tuple(x) for x in prerequisites):
            graph[s].append(e)
            num_of_depends[e] += 1
        # collect courses not depended by any other course
        # base_courses collects courses that can be taken in this iteration
        base_courses  =  [i for i in range(0, numCourses) if not num_of_depends[i]]
        for node in base_courses:
            for pre_course in graph[node]:
                # if there's base_course encountered as a pre_course
                # obviously this course graph fails
                if pre_course in base_courses: 
                    return False
                # removed checked dependency count by 1
                num_of_depends[pre_course] -= 1
                # if all deps to this pre_course were checked
                # it means there is no way cyclic back to this course
                if num_of_depends[pre_course] == 0:
                    base_courses.append(pre_course)
        return len(base_courses) == numCourses