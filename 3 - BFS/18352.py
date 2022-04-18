import sys

n,m,k,x = map(int,sys.stdin.readline().split())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)] # 인덱스값이 노드 번호
for i in line: 
    graph[i[0]].append(i[1]) # 단방향


seen = [0] * (n+1)
def sol(n,k) : #시작거리, 최단거리
    queue = [n]
    seen[n] = 1
    count = 0
    while queue :
        result = []
        count += 1
        #x = queue.pop(0)
        for i in queue :
            for j in graph[i] :
                if seen[j] == 0 :
                    seen[j] = 1
                    result.append(j)
        queue = result
        if count == k : 
            #return result
            # 여기서 리턴하면 (AttributeError) - while문이 실행되지않았을때 반환값이 없음ㅁ
            break
        
    return result

result = sol(x,k)
# result = sol(x,k).sort() 이거하면 none됨 왜???
result.sort()

if result :
    for i in result :
        print(i)
else : print(-1)