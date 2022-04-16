from collections import deque
import sys
n,m,v = map(int,sys.stdin.readline().split())
p = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)] # 빈 배열 초기화 가능?

# make adjacency list
for i in p:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
# sort adjacency list
for i in range(1, n+1):
    graph[i].sort()


def dfs(v,seen):
    seen[v] = True # 담는거 보다 인덱스로 표현하는게 찾을때 더 빨라서?
    print(v,end=' ')
    for i in graph[v] :
        if not seen[i]:
            dfs(i,seen)
            

def bfs(v,seen):
    queue = deque([v])
    seen[v] = True
    while queue :
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v] :
            if not seen[i] :
                queue.append(i)
                seen[i] = True



seen = [False] *(n+1)
dfs(v,seen)
print()
seen = [False] *(n+1)
bfs(v,seen)

