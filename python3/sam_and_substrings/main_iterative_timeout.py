import sys

def substrings(balls):
    # Complete this function
    n = len(balls)
    total_sum = 0
    for i in range(n-1, -1, -1):
        pow_sum = 0
        for j in range(0, n-i):
            pow_sum += (n-((n-1)-i)) * pow(10, j)
        total_sum += int(balls[i]) * pow_sum
    return total_sum % (pow(10, 9)+7)

if __name__ == "__main__":
    balls = input().strip()
    result = substrings(balls)
    print(result)