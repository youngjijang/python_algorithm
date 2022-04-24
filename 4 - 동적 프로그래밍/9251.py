import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]
# print(dp)

for i in range(1, len(b)+1) :
    for j in range(1, len(a)+1) :
        if a[j-1] == b[i-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[len(b)][len(a)])

# dp2 = [0] * len(a)+1

# for i in range(len(a)):
#     for j in range(len(b)) :
