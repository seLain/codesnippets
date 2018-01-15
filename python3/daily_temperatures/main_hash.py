import bisect

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        if n == 0:
            return []
        elif n == 1:
            return [0]

        # get the y axis of temperatures figure
        dict_temperatures = {}  # {temperature:[index1, index2, ...]}
        for i in range(0, len(temperatures)):
            if temperatures[i] in dict_temperatures.keys():
                dict_temperatures[temperatures[i]].append(i)
            else:
                dict_temperatures[temperatures[i]] = [i]

        # ordering occurred temperatures
        ordered_temperatures = sorted(dict_temperatures.keys())

        # do computation
        wait_days = []
        for i in range(0, n-1):
            current_temp = temperatures[i]
            current_temp_idx = ordered_temperatures.index(current_temp)
            if current_temp_idx == len(ordered_temperatures)-1: # no more higher temperature
                wait_days.append(0)
            else:
                # get idx of nearest higher temperature
                nearest_higher_idx = n # default idx > size of temperatures dataset
                for higher_temp in ordered_temperatures[current_temp_idx+1:]:
                    for x in dict_temperatures[higher_temp]:
                        if x > i and nearest_higher_idx > x:
                            nearest_higher_idx = x
                            break
                # find idx of the nearest higher temperature
                if nearest_higher_idx == n:
                    wait_days.append(0)
                else:  # sort for the smallest idx
                    wait_days.append(nearest_higher_idx-i)

        # the last one must be 0
        wait_days.append(0)

        return wait_days



