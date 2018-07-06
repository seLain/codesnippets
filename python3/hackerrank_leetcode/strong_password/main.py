#!/bin/python3

# Hackerrank
# https://www.hackerrank.com/challenges/strong-password/problem

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    needed = 0
    if not any(char.isdigit() for char in password):
        needed += 1
    if not any(char.islower() for char in password):
        needed += 1
    if not any(char.isupper() for char in password):
        needed += 1
    if not any(char in "!@#$%^&*()-+" for char in password):
        needed += 1
    return needed if n + needed >= 6 else 6 - n

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)