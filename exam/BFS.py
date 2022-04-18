# 인접 행렬
def bfs(graph, input_start) :
    visited = [False] * len(graph)
    answer = []

    queue = [input_start]
    visited[input_start] = True
    while queue :
        node = queue.pop(0) #큐 - 맨처음 들어간 데이터 pop
        answer.append(node)
        for i in range(len(graph[node])) :
            if graph[node][i] == 1 and not visited[i] and node != i :
                queue.append(i)
                visited[i] = True
    return answer


graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]]

print('경로 : ',end='')
print(bfs(graph,0))

######################################
# 주어진 그래프의 시작 정점부터, n번만에 갈 수 있는 노드 
def sol (graph, input_start,n) :
    visited = [False] * len(graph)
    queue = [input_start]
    visited[input_start] = True
    count = 0

    while queue :
        count += 1
        new_arr = []
        for i in queue :
            node = i
            for j in range(len(graph[node])) : #다음 카운트에 가능한 모든 경우를 확인
                if graph[node][j] == 1 and not visited[j] and node != j :
                    new_arr.append(j)
                    visited[j] = True

        queue = new_arr #해당 카운트에 가능한 노드 저장됨
        if count == n : return new_arr


graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]]

print(sol(graph,1,3))