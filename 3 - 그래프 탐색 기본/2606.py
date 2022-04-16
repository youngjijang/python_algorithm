import sys

computer = int(sys.stdin.readline())
line = int(sys.stdin.readline())

graph = [[]for _ in range(computer+1)] #앞에 0 인덱스 포함 무시하고 생성
# print(b)
for _ in range(line) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
def dfs(v,seen):# 연결된 인데스 까지만 돔
    seen[v] = True 
    # print(v,end=' ')
    global count
    count += 1
    for i in graph[v] :
        if not seen[i]:
            dfs(i,seen)

seen = [False] * (computer+1)
dfs(1,seen)
print(count-1) #1번빼고