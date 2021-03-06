import sys

def substrings(balls):
    # Complete this function
    int_balls = [int(x) for x in balls]
    n = len(int_balls)
    total_sum = 0
    pow_sum = 0
    mod_val = pow(10, 9)+7
    for i in range(n-1, -1, -1):
        pow_sum += pow(10, n-1-i)
        total_sum += (int_balls[i] * (i+1) * pow_sum) % mod_val
    return total_sum % mod_val

if __name__ == "__main__":
    balls = input().strip()
    result = substrings(balls)
    print(result)