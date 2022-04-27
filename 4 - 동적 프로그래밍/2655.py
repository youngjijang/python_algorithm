# 가장 높은 탑쌓기
# 저장해야할 값이 많아서 헷갈린다. dict에 저장하고 싶었는데 더 헷갈려 그냥 배열에 저장해라

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    a,b,c = map(int,sys.stdin.readline().split())
    arr.append([a,b,c,i+1])

arr.sort(key=lambda x : x[0])
# print(sort_top)

# for i in range(n) :
#     h = sort_top[i][1]
#     for j in range(n) :
#         if sort_top[j][2] < sort_top[i][2] :
#             h += sort_top[j][1]

