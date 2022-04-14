import math
x = int(input())
a = [[*map(int,input().split())] for _ in range(x)]

####### 2중 for문 돌리기 ########
# distances = []
# mini = 1000000000000
# for i in range(x) :
#     for j in range(i+1,x) :
#         result = math.pow(int(a[i][0])-int(a[j][0]),2) + math.pow(int(a[i][1])-int(a[j][1]),2)
#         if result < mini :
#             mini = result
# print(int(mini))


########## 다른 방법 > 시간 초과
# 1. 좌표 정렬
# 2. 임의의 거리(최소값) 구하기 
# 3. for문으로 해당 좌표로 부터 최소거리 내에 있는 좌표 확인
# 4. 최소 거리보다 더 작은 좌표가 있을떄 업데이트 (0이 나오면 더 짧은거리는 없으니까 break)
# 5. for문 다 돌면 끝

a.sort()
# print(a)
# mini = math.pow(a[0][0]-a[1][0],2) + math.pow(a[0][1]-a[1][1],2)

# def sol(x,y) : #x,y는 각각 위치 좌표 - 일차배열
#     global mini
#     #길이가 mini 보다 작은지 확인
#     if  math.pow(x[0]-y[0],2) + math.pow(x[1]-y[1],2) < mini :
#         return True
#     return False

# def dis() :
#     global mini
#     for z in range(len(a)) :
#         i = a[z]
#         for j in range(z+1,len(a)) :
#             if a[j][0] <= i[0] + int(math.sqrt(mini)) :
#                 if sol(i,a[j]) : 
#                     mini = math.pow(i[0]-a[j][0],2) + math.pow(i[1]-a[j][1],2)
#                     if mini == 0 : return

# dis()
# print(int(mini))


###############정답을 찾아보자
def dis(x,y) : # 1차원 배열
   return (x[0]-y[0])**2 + (x[1]-y[1],2)**2

def closer(start, end) :
    if start == end :
        return float('inf')

    if end - start == 1 :
        return dis(start,end)

