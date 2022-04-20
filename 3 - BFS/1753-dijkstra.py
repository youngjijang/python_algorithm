import heapq
import sys

n,e = map(int,sys.stdin.readline().split()) #정점개수/간선개수
k = int(sys.stdin.readline())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(e) :
    u,v,w = map(int,sys.stdin.readline().split()) #u에서 v로 가는 가중치w
    graph[u].append((w,v))

# print(graph)
INF = int(10e7)
distance = [INF] * (n+1)
distance[k] = 0
heap = []
heapq.heappush(heap,(0,k))
# answer = []
while heap :
    dis, cur = heapq.heappop(heap)
    # answer.append(dis)

    if distance[cur] < dis :
        continue
    
    for i in graph[cur] :
        if distance[i[1]] > i[0]+dis :
            distance[i[1]] = i[0]+dis
            heapq.heappush(heap,(i[0]+dis,i[1]))

for i in range(1,n+1) :
    if distance[i] == INF :
        print('INF')
    else :         
        print(distance[i])