# 마이너스 뒤에 다음 마이너스 나올때까지 플러스 괄호안에 ?
import sys
a = list(sys.stdin.readline().split('-')) #마이너스 기준으로 나눔

# print(a)

num = []
for i in a :
    if '+' in list(i) :
        nums = list(map(int,i.strip().split('+'))) #나눈 리스트중에 + 있나 확인하고 먼저 연산 수행(괄호치기)
        num.append(sum(nums))
    else : num.append(int(i))

# print(num)
result = num[0]
for i in range(1,len(num)) :
    result -= num[i] #나머지 리스트들 -연산 수행

print(result)