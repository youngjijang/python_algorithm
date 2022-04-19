import heapq
import sys
#다익스트라
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
buslist = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
start, end = map(int,sys.stdin.readline().split())

INF = int(1e9)
####### 인접행렬
# graph = [[INF]*m for _ in range(n+1) ]
# for i in buslist :
#     graph[i[0]][i[1]] = i[2] 

###### 인접 리스트
graph = [[]*m for _ in range(n+1)]
for i in buslist :
    graph[i[0]].append((i[1],i[2])) #튜플???

# 입력받으면서 저장하는 방식##########
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b, c))

print(graph)
distance = [INF] * (n+1) # 각 노드로 가는 최소 값 저장

def dijkstra(start) : #다익스트라 - 우선순위 큐(힙)을 이용해 최소값 구하기 O(logN)
        q = []
        #시작노드로 가기 위한 최단경로 0으로 설정
        heapq.heappush(q,(0,start)) # 거리,노드 순으로 넣는 이유 : heapq 모듈에 첫번째 데이터를 기준으로 정렬됨
        distance[start] = 0

        while q : 
            #가장 낮은 거리를 가진(힙 최소값) 노드와 거리를 추출
            dist, now = heapq.heappop(q)

            if distance[now] < dist : 
                continue #저장된 거리와 추출된 거리와 비교하여 저장된 거리가 더 작다면 비교하지않고 바로 넘어감 (이미 방문한 노드 체크   )
            
            for i in graph[now] : #대상에서 인접한 노드와 거리 순회
                cost = dist + i[1] #이전까지의 거리 + 해당 전선의 거리 
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
                    print(q)

dijkstra(start)
print(distance)