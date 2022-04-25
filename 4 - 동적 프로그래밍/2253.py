import sys

n,m = map(int,sys.stdin.readline().split())
small = [int(sys.stdin.readline()) for _ in range(m)]
INF = int(10e7)
a = int((2 * n)** 0.5) + 1
dp = [[INF]*(a+1)for _ in range(n+1)]

dp[1][0] = 0

for i in range(2,n+1) :
    if i in small :#####!!!!
        continue
    for v in range(1,a) : #0부터했더니 INF 
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1])+1

result = min(dp[n])
if result == INF : print(-1)
else : print(result)