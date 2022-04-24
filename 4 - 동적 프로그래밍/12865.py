import sys

n,k = map(int,sys.stdin.readline().split())
t = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

maxi = 0
dp = [[0]*(k+1) for _ in range(n+1)]
# print(t)
for i in range(1,n+1) : #물건 
    for j in range(1,k+1) : #무게
        w = t[i-1][0]
        v = t[i-1][1]

        if w > j : #무게 보다 크면 못 넣음
            dp[i][j] =  dp[i-1][j]
        else : #무게보다 작을 경우 뭐가 더 나은지 고르기
            dp[i][j] =  max(dp[i-1][j],dp[i-1][j-w]+v)
            # 현재 넣을 무게 만큼 뺀 배낭에는 그 무게의 배낭이 가지는 최대 가치라 저장되어있어 상관없다..........>???>>>>>!!!!!


print(dp[n][k])