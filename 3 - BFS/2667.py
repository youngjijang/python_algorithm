import sys

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]


# visited = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향

##########스택
stack = []
def dfs(x,y) :
    count = 1
    while stack :
        x,y = stack.pop()
        l[x][y] = '0'
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and l[xx][yy] == '1' :
                l[xx][yy] = '0'
                stack.append((xx,yy))
                count += 1
    return count 

###########재귀
def recursive(x,y,count) :
    l[x][y] = '0'
    count += 1
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and l[xx][yy] == '1' :
            count = recursive(xx,yy,count)
    return count


num = []
count = 0
# print(l)
# print(visited)
for i in range(n) :
    for j in range(n) :
        if l[i][j] == '1' :# and not visited[i][j] :
            # stack.append((i,j))
            num.append(recursive(i,j,0))
            count += 1

print(count)
num.sort()
for i in num :
    print(i)



