import sys
sys.setrecursionlimit(10000)

def passwordCracker(passwd, attempt):
    # Complete this function
    if attempt == '':
        return True, []
    
    new_attempt = attempt
    for p in passwd:
        if p in new_attempt:
            p_index = new_attempt.index(p)
            partition_1 = new_attempt[0:p_index]
            passed_1, constitutes_1 = passwordCracker(passwd, partition_1)
            if passed_1:
                partition_2 = new_attempt[p_index+len(p):]
                passed_2, constitutes_2 = passwordCracker(passwd, partition_2)
                if passed_2:
                    return True, constitutes_1 + [p] + constitutes_2
            
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