
import sys
n,m = map(int,sys.stdin.readline().split())
ice = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c_ice = [[0]*(m) for _ in range(n)]

seen = [[0]*m for _ in range(n) ]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향



# stack = [[0,0]]
# seen[0][0] = 1
# while stack : 
#     x,y = stack.pop()
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if  0 <= nx < n and 0 <= ny < m:
#             if seen[nx][ny] == 0 and ice[nx][ny] == 0 :
#                 seen[nx][ny] = 1
#                 c_ice
#                 stack.append((nx,ny))
def dfs(x,y) :
    pass



count = 0
for i in range(n) :
    for j in range(m) :
        if ice[i][j] != 0 and seen[i][j] == 0:
            seen[i][j] = 1
            stack = [[i,j]]
            dfs(i,j)
            count += 1
        if count >= 2 : 
            print()
            exit(0)

if count == 0 :
    print(0)
            

