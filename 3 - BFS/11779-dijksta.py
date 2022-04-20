import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split()) #출발도시/도착도시/버스비용
    graph[a].append((c,b))

start,end = map(int,sys.stdin.readline().split())
# print(graph)

INF = int(10e7)
distance = [INF] * (n+1)
distance[start] = 0
heap = []
heapq.heappush(heap,(0,start))
trace = [[]*(n+1) for _ in range(n+1)] # 최단 비용일때 경로 저장하기
for i in range(1,n+1) :
    trace[i].append(i) # 자기자신으로 초기화 
    # 다음 노드의 최단경로 = 현재까지 누적 경로 + 다음 노드
    #trace[next] = trace[cur] + [next]

while heap :
    dis, cur = heapq.heappop(heap)

    if distance[cur] < dis :
        continue
    
    for i in graph[cur] :
        if distance[i[1]] > i[0]+dis :
            distance[i[1]] = i[0]+dis
            heapq.heappush(heap,(i[0]+dis,i[1]))
            trace[i[1]] = trace[cur] + [i[1]]

print(distance[end])
print(len(trace[end]))
print(*trace[end])