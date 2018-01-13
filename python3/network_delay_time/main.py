class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dict_times = {} # key: [visited, shortest_time_to_this_node, (next_node, time), ...]
                        # for ex: {1: [True, 2, (3, 1), (4, 2)]}
        for i in range(1, N+1):
            dict_times[i] = [False, 0]
        for t in times:
            dict_times[t[0]].append((t[1], t[2]))

        next_nodes = [K]
        dict_times[K][0] = True
        while len(next_nodes) > 0:
            current_nodes = next_nodes
            next_nodes = []
            for n in current_nodes:
                for edge in dict_times[n][2:]:
                    expected_time = dict_times[n][1] + edge[1]
                    if dict_times[edge[0]][0] is False:
                        dict_times[edge[0]][0] = True
                        dict_times[edge[0]][1] = expected_time
                        next_nodes += [edge[0]]
                    else:
                        if dict_times[edge[0]][1] > expected_time:
                            dict_times[edge[0]][1] = expected_time
                            next_nodes += [edge[0]]
        # check if all covered
        for n in dict_times.keys():
            if dict_times[n][0] is False:
                return -1 

        # all covered, find the largest time
        largest_time = 0
        for n in dict_times.keys():
            if largest_time < dict_times[n][1]:
                largest_time = dict_times[n][1]
        return largest_time