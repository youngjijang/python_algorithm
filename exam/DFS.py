
# stack 이용 , 인접 행렬
def iterative_dfs(graph, input_start) :
    visited = [0] * len(graph) # 방문 체크 0으로 초기화
    answer = [] 

    stack = [input_start] # 노드 번호가 들어감
    while stack :
        temp = stack.pop()
        visited[temp] = 1 #방문했으면 1
        answer.append(temp)

        for i in range(len(graph[temp])) :
            if graph[temp][i] == 1 and visited[i] == 0 and temp != i : #에지(간선)가 있고/방문안했고/자기자신 제외
                stack.append(i)
    return answer

graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]] # 인접 행렬

# print('경로 : ',end='')
# print(iterative_dfs(graph,0))       


################################################
#재귀 이용
def recursive_dfs (graph,start,visited,answer) :
    visited[start] = 1
    answer.append(start)

    for i in range(len(graph[start])) :
        if graph[start][i] == 1 and visited[i] == 0 and start != i : #길이 있는지 확인해 준다. graph[start][i] == 1
            recursive_dfs(graph,i,visited,answer)

graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]] #인접 행렬

visited = [0] *len(graph) #초기화는 한번만 실행되야하니까 함수밖에 선언
answer = []

recursive_dfs(graph,0,visited,answer)
print('경로 : ',end='')
print(answer) # 재귀랑 스택 결과가 다른 이유는 ~ 그거

########################################33

# 인접 리스트 , 재귀

def list_dfs (graph,start,visited,answer) :
    visited[start] = 1
    answer.append(start)
    for i in graph[start] :
        if visited[i] == 0 and start != i : #해당노드를 방문한적 있는지 / 자기자신 제외
            list_dfs(graph,i,visited,answer)

graph = [[0,1,2,3],
         [0,1],
         [0,2,5],
         [0,3,4],
         [3,4],
         [2,5]] #인접 리스트

visited = [0] *len(graph)
answer = []
list_dfs(graph,0,visited,answer)
print('경로 : ',end='')
print(answer)


####################################
#dfs로 모든 경로 구하기 - 재귀가 편하다
