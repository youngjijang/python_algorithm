from collections import defaultdict
import sys

n,m = map(int,sys.stdin.readline().split())
biz = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
center = n//2 + 1
# graph =[[]*(n+1) for _ in range(n+1)] # 무거운순
# graph2 =[[]*(n+1) for _ in range(n+1)] # 가벼우순
light = defaultdict(list) #defauldict을 사용해서 선언 
heavy = defaultdict(list)
for i,j in biz :
    light[i].append(j) 
    heavy[j].append(i) #없으면 빈 리스트로 저장
# print(light)
# print(heavy)
def dfs(a,dict) : # 무거운순 깊이 탐색해서 자식 노드 몇개인지 answer에 담기
    visited[a] = 1
    answer.append(a)
    for i in range(len(dict[a])) :
        if visited[dict[a][i]] == 0 :
            dfs(dict[a][i],dict) #없으면 빈 리스트

count = 0
for i in range(n) :
    answer = []
    visited = [0]*(n+1)
    dfs(i+1,light)
    # print(answer)
    if len(answer) > center : # 자식 노드 개수가 전체개수/2 보다 크면 카운트
        count += 1

for i in range(n) :
    answer = []
    visited = [0]*(n+1)
    dfs(i+1,heavy)
    # print(answer)
    if len(answer) > center :
        count += 1

print(count)