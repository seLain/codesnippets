class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val_list = []
        self.min_index_list = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val_list.append(x)
        # maintain min index list
        if len(self.min_index_list) == 0:
            self.min_index_list.append(0)
        else:
            if self.val_list[self.min_index_list[-1]] > x:
                self.min_index_list.append(len(self.val_list)-1)
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.val_list) > 0:
            val = self.val_list[-1]
            # maintain min index list
            if self.min_index_list[-1] == len(self.val_list)-1:
                del self.min_index_list[-1]
            # do stack pop
            del self.val_list[-1]
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.val_list) > 0:
            return self.val_list[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_index_list) == 0:
            return None
        else:
            return self.val_list[self.min_index_list[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()