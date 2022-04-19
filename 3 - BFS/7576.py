from collections import deque

import sys

m,n = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향

q = deque([])
visited = [[False]*(m) for _ in range(n) ]

def sol() :
    global n,m
    while q :
        cur = q.popleft() # 현재 값
        for i in range(4) :
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[1]
            if 0 <= xx <n and 0 <= yy < m and not visited[xx][yy] and tomato[xx][yy] == 0 :
                tomato[xx][yy] = 1
                visited[xx][yy] = True
                q.append((xx,yy,cur[2]+1))
    return cur[2]


for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            q.append((i,j,0))
            visited[i][j] = True

result = sol()

for i in tomato :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
print(result)
# print(tomato)