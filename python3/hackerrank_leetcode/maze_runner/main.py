'''
Maze:

.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.

Legend:
M - start
* - destination
. - path
X - block

'''
import sys

def go(matrix, path_stack, p_idxs):
    current_idx = path_stack[-1]
    # out of bound check
    if current_idx[0] < 0 or current_idx[0] >= len(matrix) or \
        current_idx[1] < 0 or current_idx[1] >= len(matrix[0]):
        path_stack.pop()
        return False
    # turing back check
    if len(path_stack) >= 3 and current_idx == path_stack[-3]:
        path_stack.pop()
        return False
    # path check
    if matrix[current_idx[0]][current_idx[1]] == 'X':
        path_stack.pop()
        return False
    elif matrix[current_idx[0]][current_idx[1]] == '*':
        return True
    else:
        path_stack.append((current_idx[0]-1, current_idx[1])) # try to go up
        go_up = go(matrix, path_stack, p_idxs)
        path_stack.append((current_idx[0], current_idx[1]+1)) # try to go right
        go_right = go(matrix, path_stack, p_idxs)
        path_stack.append((current_idx[0]+1, current_idx[1])) # try to go down
        go_down = go(matrix, path_stack, p_idxs)
        path_stack.append((current_idx[0], current_idx[1]-1)) # try to go left
        go_left = go(matrix, path_stack, p_idxs)
        if go_up or go_right or go_down or go_left:
            return True
        else:
            path_stack.pop()
            return False

def countLuck(matrix):
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
    is_found = go(matrix, path_stack, p_idxs) # map, path, destination
    print(is_found)
    # return direction change

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
        result = countLuck(matrix)
        print(result)