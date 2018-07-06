'''
Hackerrank problem: count luck
https://www.hackerrank.com/challenges/count-luck/problem
'''
import sys

def go(matrix, path_stack, p_idxs, count):
    #print(path_stack)
    current_idx = path_stack[-1]
    # out of bound check
    if current_idx[0] < 0 or current_idx[0] >= len(matrix) or \
        current_idx[1] < 0 or current_idx[1] >= len(matrix[0]):
        path_stack.pop()
        return False, count
    # turing back check
    if len(path_stack) >= 3 and current_idx == path_stack[-3]:
        path_stack.pop()
        return False, count
    # path check
    if matrix[current_idx[0]][current_idx[1]] == 'X':
        path_stack.pop()
        return False, count
    elif matrix[current_idx[0]][current_idx[1]] == '*':
        return True, count
    else:
        up = (current_idx[0]-1, current_idx[1])
        right = (current_idx[0], current_idx[1]+1)
        down = (current_idx[0]+1, current_idx[1])
        left = (current_idx[0], current_idx[1]-1)
        # check if there is multiple choices, if yes, increase the counter
        choice_count = 0
        for d in [up, right, down, left]:
            if d[0] < 0 or d[0] >= len(matrix) or d[1] < 0 or d[1] >= len(matrix[0]):
                continue
            elif len(path_stack) >= 3 and d == path_stack[-2]:
                continue
            elif matrix[d[0]][d[1]] == '.' or matrix[d[0]][d[1]] == '*':
                choice_count += 1
        if choice_count > 1:
            count += 1
        # choose path to try
        path_stack.append(up) # try to go up
        is_found, count = go(matrix, path_stack, p_idxs, count)
        if is_found:
            return True, count
        path_stack.append(right) # try to go right
        is_found, count = go(matrix, path_stack, p_idxs, count)
        if is_found:
            return True, count
        path_stack.append(down) # try to go down
        is_found, count = go(matrix, path_stack, p_idxs, count)
        if is_found:
            return True, count
        path_stack.append(left) # try to go left
        is_found, count = go(matrix, path_stack, p_idxs, count)
        if is_found:
            return True, count
        else:
            # all four direction failed
            if choice_count > 1: # if this failed cell has multiple choices, decrease it
                count -= 1
            path_stack.pop()
            return False, count

def countLuck(matrix, k):
    # Complete this function
    # get location of M and *
    m_idxs = (-1, -1)
    p_idxs = (-1, -1)
    for i in range(len(matrix)):
        if 'M' in matrix[i]:
            m_idxs = (i, matrix[i].index('M'))
        if '*' in matrix[i]:
            p_idxs = (i, matrix[i].index('*'))
    # find path and count direction change
    path_stack = [m_idxs]
    is_found, count = go(matrix, path_stack, p_idxs, 0) # map, path, destination
    # return direction change
    if count == k:
        return 'Impressed'
    else:
        return 'Oops!'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        matrix = []
        matrix_i = 0
        for matrix_i in range(n):
            matrix_t = str(input().strip())
            matrix.append(matrix_t)
        k = int(input().strip())
        result = countLuck(matrix, k)
        print(result)