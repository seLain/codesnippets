import sys
sys.setrecursionlimit(10000)

visited = []

def passwordCracker(passwd, attempt):
    # Complete this function
    if attempt == '':
        return True, []
    
    # already visited, but search is not ended, 
    # therefore this attempt must be false
    if attempt in visited:
        return False, []
    
    for p in passwd:
        new_attempt = attempt
        if new_attempt.startswith(p):
            new_attempt = new_attempt[len(p):]
            passed, constitutes = passwordCracker(passwd, new_attempt)
            if passed:
                return True, [p] + constitutes
            else:
                visited.append(new_attempt)
            
    return False, []

if __name__ == "__main__":
    global visited
    t = int(input().strip())
    for a0 in range(t):
        visited = [] # be sure to empty memory after at each test case
        n = int(input().strip())
        passwd = input().strip().split(' ')
        attempt = input().strip()
        passed, constitutes = passwordCracker(passwd, attempt)
        if passed:
            print(' '.join(constitutes))
        else:
            print('WRONG PASSWORD')