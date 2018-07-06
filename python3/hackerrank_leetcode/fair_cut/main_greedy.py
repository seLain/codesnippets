n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
if m > n // 2:
    m = n - m
arr = list(map(int, input().strip().split(' ')))
arr = sorted(arr)
dp = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
dp[0][0] = 0
for i in range(0, n):
    for j in range(0, i + 1):
        if j > m or i - j > n - m:
            continue
        temp_li = dp[i][j] + arr[i] * (i - j - (n - m - (i - j)))
        temp_lu = dp[i][j] + arr[i] * (j - (m - j))
        if dp[i + 1][j + 1] > temp_li:
            dp[i + 1][j + 1] = temp_li
        if dp[i + 1][j] > temp_lu:
            dp[i + 1][j] = temp_lu

print(dp[n][m])