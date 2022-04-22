# 케빈베이크의 6단계 법칙
# 다익스트라
import heapq
import sys

n,m = map(int,sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(10e7)
def sol(start) :
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap :
        dis,cur = heapq.heappop(heap)
        if distance[cur] < dis :
            continue    
        for i in graph[cur] :
            if distance[i] > dis+1 :
                distance[i] = 1+dis
                heapq.heappush(heap,(1+dis,i))


   
min = 10000000
for i in range(1,n+1) :
    distance = [INF] * (n+1)
    sol(i)
    a = sum(distance[1:])
    # print(a)
    if  a < min :
        min = a
        result = i

print(result)


#########################BFS로만 풀이

import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res))+1)