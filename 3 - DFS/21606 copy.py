import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().strip()))  #실내1 실외0 - 인덱스+1가 노드번호
# print(A)
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]

graph = [[] for _ in range(n+1)] # 인덱스값이 노드 번호
for i in arr: #그래프를 인접리스트로 표현하기
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0]) 

# print(graph)
count = 0

def dfs(v) : #시작노드번호
    global count
    num = 0
    seen[v] = True
    # print(v,end=' ')
    for i in graph[v] : #i는 연결된 노드번호
        if not seen[i] :
            if A[i-1] == 0 : 
                 num += dfs(i)#!!!!!헷갈리지말기!!!
            elif A[i-1] == 1 : 
                num += 1
    return num


seen = [False] * (n+1) #인덱스 값이 노드 번호
for i in range(n) :
    if A[i] == 1 : 
        for j in graph[i+1] :
            if A[j-1] == 1 : count += 1 # A 인덱스는 0 부터 시작함
    else : 
        if not seen[i+1] : #!!!!!!!!!!!!!!!!!!왜--
            r =  dfs(i+1)
            count += r*(r-1)

print(count)