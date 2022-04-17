
import sys

n,m = map(int,sys.stdin.readline().split())
miro = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]

seen = [[0]*(m) for _ in range(n) ]
# print(seen)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향
count = 0

queue = [[0,0]]
seen[0][0] = 1

while queue :
    x,y = queue.pop(0)
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if seen[nx][ny] == 0 and miro[nx][ny] == 1:
                seen[nx][ny] = seen[x][y] + 1
                queue.append((nx,ny))

# print(seen)

print(seen[n-1][m-1])


