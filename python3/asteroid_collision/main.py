class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        if n == 0:
            return []
        elif n == 1:
            return asteroids
        else:
            stack = []
            for x in asteroids:
                if len(stack) == 0:
                    stack.append(x)
                else:
                    if x > 0:
                        stack.append(x)
                    elif x < 0:
                        while len(stack) > 0:
                            if stack[-1] < 0:
                                stack.append(x)
                                break   # ignore x, next x
                            elif stack[-1] > 0:
                                if abs(stack[-1]) > abs(x):
                                    break # ignore x, do nothing
                                elif abs(stack[-1]) == abs(x):
                                    stack.pop() # remove stack[-1]
                                    break   # ignore x, next x
                                elif abs(stack[-1]) < abs(x):
                                    stack.pop() # remove stack[-1], continue x
                                    if len(stack) == 0: # if all elements were removed
                                        stack.append(x)
                                        break
            return stack
