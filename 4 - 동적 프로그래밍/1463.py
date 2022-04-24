import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1) #dp[n]은 n이 되기위한 최소 연산 횟수
# dp[1] = 1 #ㅇ
for i in range(1,n+1) :
    dp[i] = dp[i-1]+1 #1일 더히는 연산 +1
    if i % 3 == 0 :
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0 :
        dp[i] = min(dp[i],dp[i//2]+1)
    # 모든 연산 경우가 다 걸려야하기때문에 if
print(dp)
