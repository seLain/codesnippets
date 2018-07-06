import sys

def candies(n, arr):
    # Complete this function
    candies = [1]*n
    # forward check
    for i in range(1, len(arr)):
        # determine candies[i] by comparison
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1
    # backward check
    for j in range(len(arr)-2, -1, -1):
        if arr[j] > arr[j+1] and candies[j] <= candies[j+1]:
            candies[j] = candies[j+1] + 1
        
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