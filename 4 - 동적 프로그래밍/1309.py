import sys

n = int(sys.stdin.readline())

dp = [[0]*2 for _ in range(n+1)]
dp[1] = [1,1,1]
for i in range(2,n+1) :
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 9901
    dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1]) % 9901

print((dp[n][0]*2 + dp[n][1])%9901)

#메모리초과 - 나머지 분배 법칙