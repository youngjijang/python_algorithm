#경쟁적 전염 #시간초과
# BFS

import heapq
import sys

n,k = map(int,sys.stdin.readline().split()) #크기, 바이러스 종류 수
b = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s,x,y = map(int,sys.stdin.readline().split()) #s초 , 좌표

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향

queue = []
    
for i in range(n) :
    for j in range(n) :
        if b[i][j] > 0 :
            heapq.heappush(queue,(0,b[i][j],i,j))


def bfs() :

    ss = len(queue)
   
    while ss :
        # print(a)
        cur = heapq.heappop(queue)
        # print(cur)
        for i in range(4) :
            xx = cur[2] + dx[i]
            yy = cur[3] + dy[i]
            if 0<=xx<n and 0<=yy<n and b[xx][yy] == 0 :
                b[xx][yy] = cur[1]
                # heapq.heappush(queue,(cur[2],xx,yy))
                queue.append((cur[0]+1,cur[1],xx,yy))
                # queue.append((xx,yy,cur[2]))
        ss -= 1


for _ in range(s) :
    bfs()

# print(b)
print(b[x-1][y-1])


