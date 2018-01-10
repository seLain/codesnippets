class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # determine the shorter list
        if len(list1) > len(list2):
            return self._findRestaurant(list2, list1)
        else:
            return self._findRestaurant(list1, list2)

    def _findRestaurant(self, list1, list2):

        dict_list1 = { list1[i]:i for i in range(0, len(list1)) }
        n2 = len(list2)
        least_sum = n2 * 2
        restaurants = []
        for i in range(0, n2):
            if list2[i] in dict_list1.keys():
                index_sum = dict_list1[list2[i]] + i
                if index_sum < least_sum:
                    least_sum = index_sum
                    restaurants = [list2[i]]
                elif index_sum == least_sum:
                    restaurants.append(list2[i])
        return restaurants
