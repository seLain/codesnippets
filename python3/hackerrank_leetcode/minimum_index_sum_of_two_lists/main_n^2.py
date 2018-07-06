class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # get all options first
        common_opts = [x for x in list2 if x in list1]
        # iterate all options to get sum index
        if len(common_opts) == 0:
            return []
        else:
            least_sum = list1.index(common_opts[0]) + \
                        list2.index(common_opts[0])
            restaurants = [common_opts[0]]
            for opt in common_opts[1:]:
                index_sum = list1.index(opt) + list2.index(opt)
                if index_sum < least_sum:
                    restaurants = [opt]
                elif index_sum == least_sum:
                    restaurants.append(opt)
            return restaurants
