#?????????????????????/암호코드

import sys

n = sys.stdin.readline().strip()
l = len(n)

if n[0] == 0 : # 얌호가 아닌 경우 맨처음 0이 나오는 경우
    print(0)
    exit()

dp = [0] *(l+1) #n번째일때 해석 가능한 경우의 수
dp[0] = 1
dp[1] = 1

for i in range(2,l+1) :
    if int(n[i-1]) > 0 : # 자기 자신만 봤을때 
        dp[i] += dp[i-1]
    if 10 <= int(''.join(n[i-2:i])) < 27 :  # 앞에 숫자랑 같이 카운트 할수있을 경우 
        # print(int(''.join(n[i-2:i])))
        dp[i] += dp[i-2] 

print(dp[l]%1000000)
