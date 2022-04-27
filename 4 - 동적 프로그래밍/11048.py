import sys

n,m = map(int,sys.stdin.readline().split())
candy = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)] 

dp[1][1] = candy[0][0]
for i in range(1,n+1) :
    for j in range(1,m+1):
        dp[i][j] = candy[i-1][j-1] + max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

print(dp[n][m])