import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

# dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]
# # print(dp)

# for i in range(1, len(b)+1) : #열
#     for j in range(1, len(a)+1) : #행
#         if a[j-1] == b[i-1] :
#             dp[i][j] = dp[i-1][j-1] + 1
#         else :
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j])

# print(dp[len(b)][len(a)])

# 일차원 배열로 만들기
# dp 테이블을 사용하는 방식이 열 단위!?!?로 사용하기 때문에 ???
# 열을 기준으로 행으로 돌아가서??? like 9084 동전

dp2 = [0] * (len(a)+1) 
# 하나의 문장을 기준으로 삼는다. 

# 누적값에 이전 위치까지의 ㅌ최대값을 계속 저장해줘야한다. 


for i in range(len(b)) :
    tmp = 0
    for j in range(1,len(a)+1) :
        if dp2[j]> tmp:
            tmp +=1
        elif b[i] == a[j-1] :
            dp2[j] = tmp +1    

print(dp2[len(a)])