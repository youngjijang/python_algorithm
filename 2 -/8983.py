from bisect import bisect_left
import sys

m,n,l = map(int,sys.stdin.readline().split())
xlist = list(map(int,sys.stdin.readline().split()))
animal = [[*map(int,sys.stdin.readline().split())] for _ in range(n)]
count = 0
print(animal)
xlist.sort()

# hunting = []
# for i in x :
#     for j in animal :
#         if j not in hunting :
#             if (abs(i-j[0]) + j[1]) <= l :
#                 hunting.append(j)
# print(hunting)

# 동물을 기준으로 줄이기 - 동물 위치에 가장 가까운 사대위치를 찾아(이분탐색) 가능여부 체크
# 1. for문에 동물 위치 돌리기
# 2. 동물 x죄표에 가장 가까운 사대위치 찾기
# 3. 영역안에 들어가는지 확인 abs(x-a)+b 하고 들어가면 count+=1 

def sol (x,y,i) :
    global l
    if abs(i-x) + y <= l :
        return True
    return False

def hunt(x,y) : 
    global count
    index = bisect_left(xlist,x) # 있을 경우 해당인덱스, 없을경우 들어갈자리
    if x >= xlist[m-1] : 
        if sol(x,y,xlist[m-1]) : count += 1 # max보다 커서 인덱스 초과할경우
    else :
        if sol(x,y,xlist[index-1]) or sol(x,y,xlist[index]) : # 앞이 가까울지 or 뒤가 가까울지(해당 값가 있는 경우 포함)
            count += 1

for i in animal :
    if i[1] <= l :
        hunt(i[0],i[1])

print(count)