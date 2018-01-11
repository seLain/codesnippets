class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        collision = True
        while collision is True:
            collision = False
            n = len(asteroids)
            if n < 2:
                return asteroids
            else:
                idx = 0
                new_asteroids = []
                while idx < n-1:
                    if asteroids[idx] > 0 and asteroids[idx+1] < 0:
                        collision = True
                        val1 = abs(asteroids[idx])
                        val2 = abs(asteroids[idx+1])
                        if val1 > val2:
                            new_asteroids.append(asteroids[idx])
                        elif val1 < val2:
                            new_asteroids.append(asteroids[idx+1])
                        idx += 2
                    else:
                        new_asteroids.append(asteroids[idx])
                        idx += 1
                        if idx == n-1:  # deal with the last element
                            new_asteroids.append(asteroids[idx])
                asteroids = new_asteroids
        return asteroids
