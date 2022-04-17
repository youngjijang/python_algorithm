import sys
n,m = map(int,sys.stdin.readline().split())
ice = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c_ice = [[0]*(m) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if ice[i][j] != 0 :
            pass