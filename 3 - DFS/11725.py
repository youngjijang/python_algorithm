import sys
sys.setrecursionlimit(10**7)

### unoin으로 풀수있나?

n = int(sys.stdin.readline())
# p = [list(map(int,sys.stdin.readline())) for _ in range(n-1)]

graph = [[]for _ in range(n+1)] #앞에 0 인덱스 포함 무시하고 생성
# print(b)
for _ in range(n-1) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

seen = [False] * (n+1)
parent = [i for i in range(n+1)] # 부모 노드 저장하는 배열
def dfs (v) :
    seen[v] = True
    for w in graph[v] :
        if not seen[w] :
            parent[w] = v
            dfs(w)

dfs(1)
for i in parent[2:] :
    print(i)