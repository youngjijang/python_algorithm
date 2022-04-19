import heapq
import sys

n = int(sys.stdin.readline())
miro = [list(sys.stdin.readline()) for _ in range(n)]
# 검은방-0 흰방-1

# 다익스트라

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향
visited = [[0]*n for _ in range(n)]

def dijkstra(x,y) :
    hq = []
    heapq.heappush(hq,(0,x,y))
    visited[x][y] = 1
    while hq :
        cur = heapq.heappop(hq)
        if cur[1] == n-1 and cur[2] == n-1 :
            return cur[0]
        for i in range(4) :
            xx = cur[1] + dx[i]
            yy = cur[2] + dy[i]
            if 0 <= xx < n and 0 <= yy <n and visited[xx][yy] == 0:
                if miro[xx][yy] == '1' :
                    visited[xx][yy] = 1
                    heapq.heappush(hq,(cur[0],xx,yy))
                elif miro[xx][yy] == '0' :
                    visited[xx][yy] = 1
                    heapq.heappush(hq,(cur[0]+1,xx,yy))


print(dijkstra(0,0))

