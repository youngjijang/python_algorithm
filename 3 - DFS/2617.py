import sys

n,m = map(int,sys.stdin.readline().split())
biz = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
center = n//2 + 1
graph =[[]*(n+1) for _ in range(n+1)] # 무거운순
for i in biz :
    graph[i[0]].append(i[1])

graph2 =[[]*(n+1) for _ in range(n+1)] # 가벼우순
for i in range(m) :
    graph2[biz[i][1]].append(biz[i][0])

# print(graph)
# print(graph2)
# center = n//2

def dfs(a) : # 무거운순 깊이 탐색해서 자식 노드 몇개인지 answer에 담기
    visited[a] = 1
    answer.append(a)
    for i in range(len(graph[a])) :
        if visited[graph[a][i]] == 0 :
            dfs(graph[a][i])



def dfs2(a) : # 가벼운순 싶이 탐색해서 각 노드마다 자식노드 담기 
    visited[a] = 1
    answer2.append(a)
    for i in range(len(graph2[a])) :
        if visited[graph2[a][i]] == 0 :
            dfs2(graph2[a][i])


count = 0
for i in range(n) :
    answer = []
    visited = [0]*(n+1)
    dfs(i+1)
    # print(answer)
    if len(answer) > center : # 자식 노드 개수가 전체개수/2 보다 크면 카운트
        count += 1

for i in range(n) :
    answer2 = []
    visited = [0]*(n+1)
    dfs2(i+1)
    # print(answer2)
    if len(answer2) > center :
        count += 1

print(count)