import sys

T = int(sys.stdin.readline())
    
for _ in range(T) :
    n = int(sys.stdin.readline()) #동전의 가지수
    a = list(map(int,sys.stdin.readline().split())) #동전 종류
    m = int(sys.stdin.readline()) #최종금액

    dp = [0]*(m+1) #금앢[]이 되기 위한 모든 방법의 수
    # dp[0] = 1

    for j in a : 
        dp[j] += 1
        for i in range(1,m+1) :
            if i - j > 0 : #목표 동전 - 동전 종류
                dp[i] += dp[i-j]

    print(dp[m])
    