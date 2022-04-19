import sys

n,m = map(int,sys.stdin.readline().split())
ice = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향


def melt(a,b) :
    changed = []
    stack =[(a,b)]
    visited[a][b] = True

    while stack :
        x,y = stack.pop()
        # print(x,y)
        for i in range(4) :
            xx = x +dx[i]
            yy = y +dy[i]
            if 0 <= xx < n and 0<=yy< m:
                if ice[xx][yy] == 0 :
                    changed.append([x,y])
                    # print(changed)
                elif ice[xx][yy] > 0 and visited[xx][yy] == False:
                    visited[xx][yy] =True
                    stack.append((xx,yy))

    for i in changed :
        if ice[i[0]][i[1]] > 0 :
            ice[i[0]][i[1]] -= 1
    # return changed

   
year = 0
# melt(1,1)

while 1 :
    visited = [[False]*(m) for _ in range(n) ]
    count = 0
    year += 1
    for i in range(n) :
        for j in range(m) :
            if ice[i][j] != 0 and visited[i][j] == False :
                melt(i,j)
                count += 1

    # print(changed)
    # print(count,ice)
    if count >= 2 : break
    if count == 0 : 
        year = 1
        break

print(year-1)