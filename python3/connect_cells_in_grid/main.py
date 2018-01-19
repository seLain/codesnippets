import sys

def visit(matrix, marked, i, j, marked_by, count):
    #print('visiting '+str((i, j))+' count:'+str(count))
    if marked[i][j][0] is True:
        return count
    else:
        marked[i][j] = (True, marked_by)
        count += 1
        for x in [i-1, i, i+1]:
            for y in [j-1, j, j+1]:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not (x == i and y == j):
                    if matrix[x][y] == 1:
                        count = visit(matrix, marked, x, y, marked_by, count)
        return count
        
def connectedCell(matrix):
    # Complete this function
    marked = []
    for i in range(0, len(matrix)):
        marked.append([])
        for j in range(0, len(matrix[0])):
            marked[i].append([False, None]) # [True, (x, y)] indicates marked by (x, y)
    
    all_counts = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                all_counts.append(visit(matrix, marked, i, j, (i, j), 0))
    return max(all_counts)

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for matrix_i in range(n):
        matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
        matrix.append(matrix_t)
    result = connectedCell(matrix)
    print(result)