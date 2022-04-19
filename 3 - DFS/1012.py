import sys
sys.setrecursionlimit(10**7)

t = int(sys.stdin.readline())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향

for _ in range(t) :
    m,n,k = map(int,sys.stdin.readline().split())

    graph = [[0]*n for _ in range(m)]
    # print(graph)
    for _ in range(k) :
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    # print(graph)


    def dfs(x,y) :
        graph[x][y] = 0
        for i in range(4) :
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n and graph[xx][yy] == 1 :
                dfs(xx,yy)

    count = 0
    for i in range(m) :
        for j in range(n) :
            if graph[i][j] == 1 :
                dfs(i,j)
                count += 1
    
    print(count)




