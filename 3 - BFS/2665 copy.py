import heapq
import sys

n = int(sys.stdin.readline())
miro = [list(sys.stdin.readline()) for _ in range(n)]
# 검은방-0 흰방-1

# BFS
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향
visited = [[0]*n for _ in range(n)]

def bfs(x,y) :
    visited[x][y] = 1
    