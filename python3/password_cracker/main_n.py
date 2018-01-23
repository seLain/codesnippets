import sys
sys.setrecursionlimit(10000)

def passwordCracker(passwd, attempt):
    # Complete this function
    if attempt == '':
        return True, []
    
    new_attempt = attempt
    for p in passwd:
        if new_attempt.startswith(p):
            new_attempt = new_attempt[len(p):]
            passed, constitutes = passwordCracker(passwd, new_attempt)
            if passed:
                return True, [p] + constitutes
            
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