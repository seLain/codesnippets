class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        print('========================')
        if n == 1:
            return 1
        elif 2 <= n <= 3:
            return 2
        else:
            # f(2k+1) = f(2k)
            if n % 2 == 1:
                n = n-1
            # prepare the list
            n_list = [x for x in range(1, n+1)]
            # compute
            remain_list = n_list
            remain = 1   # 0: left, 1:right
            while len(remain_list) > 1:
                if remain == 0:
                    remain_list = sorted([remain_list[i] for i in range(len(remain_list)-2, -1, -2)])
                    remain = 1
                elif remain == 1:
                    remain_list = [remain_list[i] for i in range(1, len(remain_list), 2)]
                    remain = 0
            return remain_list[0]