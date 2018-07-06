'''
This solution can only work for some test cases
'''
import sys

def candies(n, arr):
    # Complete this function
    candies = [1] + [0]*(n-1)
    for i in range(1, len(arr)):
        # determine candies[i] by comparison
        #print('i:'+str(i)+' i-1:'+str(i-1)+' arr[i]:'+str(arr[i])+' arr[i-1]:'+str(arr[i-1]))
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1]+1
        elif arr[i] == arr[i-1]:
            candies[i] = candies[i-1]-1
        else:
            candies[i] = 0 if candies[i-1] == 1 else 1
        # check validity of candies[i]
        # if not valid, fix and go backward to check
        if candies[i] == 0:
            candies[i] = 1
            for j in range(i-1, -1, -1):
                if arr[j] > arr[j+1] and candies[j] <= candies[j+1]:
                    candies[j] = candies[j+1] + 1
                elif arr[j] <= arr[j+1]:
                    break
    return sum(candies)

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)