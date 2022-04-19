from collections import deque
import sys

m,n,h = map(int,sys.stdin.readline().split())

tomato = [[]*n for _ in range(h)]

for i in range(h) :
    for j in range(n) :
        l = list(map(int,sys.stdin.readline().split()))
        tomato[i].append(l)
# print(tomato)

dx, dy, dh = [-1, 1, 0, 0,0,0], [0, 0, -1, 1,0,0],[0,0,0,0,1,-1] #방향

q = deque([])

for a in range(h) :
    for b in range(n) :
        for c in range(m) :
            if tomato[a][b][c] == 1 :
                q.append((a,b,c,0))

# print(q)

while q :
    cur = q.popleft()
    for i in range(6) :
        xx = dx[i] + cur[1]
        yy = dy[i] + cur[2]
        hh = dh[i] + cur[0]
        if 0 <= xx < n and 0 <= yy < m and 0 <= hh < h :
            if tomato[hh][xx][yy] == 0 :
                tomato[hh][xx][yy] = 1
                q.append((hh,xx,yy,cur[3]+1))

# print(tomato)
for i in tomato :
    for j in i :
        for z in j :
            if z == 0 : 
                print(-1)
                exit(0)

print(cur[3]) 