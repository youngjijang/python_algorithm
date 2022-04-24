import sys

n = int(sys.stdin.readline())
h = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(0,n+1) :


        dp[i][j] = 2**32 
        for k in range(i,i+j) :
            dp[i][j] = min(dp[i][j], 
                             dp[i][k] + dp[k+1][j] + h[i][0] * h[k][1] * h[j][1])
    

print(dp[1][n])