import sys

n,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

# trees.sort()

#start,end 변수를 인덱스값이 아닌 데이터 값을 담는다. 
start = 1
end = max(trees)#!!!!!!!!!!!!!!!!

#target이 주어지지않고 구하는 것이 목적이기때문에 mid변수를 이용하는 형태
while start <= end : # 교차될때서야 while문 깨짐
    mid = (start+end)//2
    # sum0 = [tree-mid if tree > mid else 0 for tree in trees ]#!!!!!!!!!!!
    sum0 = [tree-mid for tree in trees if tree > mid ]
    sum_value = sum(sum0)
    if sum_value >= m : #원하는 높이 보다 더 많이 잘림 #같을 경우 넘어갔다가 다시옴
        start = mid + 1
    # elif sum_value == m :
    #     end = mid
    #     break
    else : 
        end = mid - 1

print(end)
############################################

# N,M = map(int,input().split())
# tree = list(map(int,input().split()))
# # print(N)
# mx,mn = max(tree),0

# while mn <= mx :
#     c = (mn+mx)//2
#     hap = 0

#     for i in tree:
#         if i> c:
#             hap += i-c

#     if hap >= M :   
#         mn = c+1
#     else : # hap < M:
#         mx = c-1

# print(mx)