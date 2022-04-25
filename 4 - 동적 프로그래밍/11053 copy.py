import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

dp = [1]*n # 자기자신만 수열인 경우


# 내 앞에 있는 숫자들 중에 제일 큰 값의 dp테이블+1을 해야함
# 내 앞에 있는 숫자들 중 나보다 작은 수 중 제일 큰 수를 어떻게 찾아야되는지 고민함 > for문을 돌면서 조건문에 따라 max값을 갱신해줘야하는지 고민함
# 그냥 나보다 작은 모든 수의 dp value를 검사해서 max값을 남김

for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))


# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]: #나보다 작은 수 중에 value가 나보다 클때 갱신
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))