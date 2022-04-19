from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
alist = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

# 인접리스트로 변경하기
graph =[[]*(n+1) for _ in range(n+1)]
for i in alist :
    graph[i[0]].append(i[1])
# print(graph)

# in_degree 구하기 - 이부분 헷갈림
in_degree = [0]*(n+1)

#시간초과
# for i in range(1,n+1) :
#     for j in range(1,n+1) :
#         for k in range(len(graph[j])) :
#             if graph[j][k] == i : #[모든 노드에대해][간선을 확인할때] = i로 가는 길이 있다면
#                 in_degree[i] += 1 #i로 향하는 간선의 개수 추가

#정리
for i in graph:
    for j in i :
        in_degree[j] += 1


# print(in_degree)

queue = deque([])
for i in range(1,n+1) :
    if in_degree[i] == 0 : queue.append(i)
# print(in_degree)
# print(stack)
ans = []
while queue :
    node = queue.popleft()
    ans.append(node)

    for i in range(len(graph[node])) :
        index = graph[node][i]
        in_degree[index] -= 1
        if in_degree[index] == 0 :
                queue.append(index)


print(*ans)
