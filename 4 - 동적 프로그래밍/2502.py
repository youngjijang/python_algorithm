import sys

d,k = map(int,sys.stdin.readline().split())

dp = [0] * (d+1)
dp[0] = [0,1]
dp[1] = [1,0]
for i in range(2,d+1) :
    dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

# print(dp)
a = dp[d][0]
b = dp[d][1]
for i in range(1,k) :
    for j in range(1,k) :
        if a*i + b*j == k :
            print(i)
            print(j+i)
            exit(0)