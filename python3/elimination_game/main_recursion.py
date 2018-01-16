class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif 2 <= n <= 3:
            return 2
        else:
            nlist = [x for x in range(1, n+1)]
            return self.reduct(nlist, 0) # 0 = right deletion

    def reduct(self, nlist, direction):
        
        if len(nlist) == 1:
            return nlist[0]

        if direction == 0:
            newlist = []
            for i in range(1, len(nlist), 2):
                newlist.append(nlist[i])
            del nlist
            return self.reduct(newlist, 1)
        elif direction == 1:
            newlist = []
            for i in range(len(nlist)-2, -1, -2):
                newlist.append(nlist[i])
            del nlist
            return self.reduct(newlist, 0)
        


