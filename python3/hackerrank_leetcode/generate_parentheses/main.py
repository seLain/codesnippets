class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left_stack = ['(' for i in range(0, n)]
        right_stack = [')' for i in range(0, n)]

        valid_counter = 0
        return_combs = self.__recursive_genParenthesis(left_stack, 
                                                       right_stack, 
                                                       valid_counter)
        return return_combs

    def __recursive_genParenthesis(self, left_stack, right_stack, valid_counter):
        '''
        print("left len:" + str(len(left_stack)) + \
              ", right len:" + str(len(right_stack)) + \
              ", counter:" + str(valid_counter))
        '''
        return_combs = []

        if len(left_stack) == 0 and len(right_stack) ==0:
            return []

        if len(left_stack) == 0:
            return [''.join(right_stack)]

        if valid_counter == 0:
            combs = self.__pop_left(left_stack[:], right_stack[:], valid_counter)
            for comb in combs:
                if comb not in return_combs:
                    return_combs.append(comb)

        elif valid_counter > 0:
            # case pop lft
            combs = self.__pop_left(left_stack[:], right_stack[:], valid_counter)
            for comb in combs:
                if comb not in return_combs:
                    return_combs.append(comb)
            # case pop right
            combs = self.__pop_right(left_stack[:], right_stack[:], valid_counter)
            for comb in combs:
                if comb not in return_combs:
                    return_combs.append(comb)

        return return_combs

    def __pop_left(self, left_stack, right_stack, valid_counter):

        prefix = left_stack.pop()
        valid_counter += 1
        return_combs = []
        combs = self.__recursive_genParenthesis(left_stack, 
                                                right_stack, 
                                                valid_counter)
        for comb in combs:
             return_combs.append(prefix+comb)
        return return_combs

    def __pop_right(self, left_stack, right_stack, valid_counter):

        prefix = right_stack.pop()
        valid_counter -= 1
        return_combs = []
        combs = self.__recursive_genParenthesis(left_stack, 
                                                right_stack, 
                                                valid_counter)
        for comb in combs:
            return_combs.append(prefix+comb)
        return return_combs
