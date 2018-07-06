import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

memory = defaultdict(list)

def passwordCracker(passwd, attempt):
    # Complete this function
    if attempt == '':
        return True, []
    
    new_attempt = attempt
    for p in passwd:
        if new_attempt.startswith(p):
            new_attempt = new_attempt[len(p):]
            if new_attempt not in memory.keys():
                passed, constitutes = passwordCracker(passwd, new_attempt)
                if passed:
                    memory[new_attempt] = constitutes
                    return True, [p] + memory[new_attempt]
            else:
                return True, [p] + memory[new_attempt]
            
    return False, []

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passwd = input().strip().split(' ')
        attempt = input().strip()
        passed, constitutes = passwordCracker(passwd, attempt)
        if passed:
            print(' '.join(constitutes))
        else:
            print('WRONG PASSWORD')