
def topological_sort(graph) :
    in_degree = [] #노드의 간선수 저장
    stack = [] # 간선이 없는 노드를 저장(indegree) - stack이 빌때까지
    answer = [] # 선택되는 스택 저장 (순서?)

    for i in range(len(graph)) : 
        temp = 0
        for col in range(len(graph)) :
            temp += graph[col][i] ##!!!!!!!!노드의 간선이 아니라 노드로 향하는 간선 확인
        in_degree.append(temp) # 각 노드의 간선수 저장 > 간선이 0인 노드를 구하기 위해서
    
    # print(in_degree)

    for i in range(len(in_degree)) :
        if in_degree[i] == 0 : stack.append(i)
        # 처음 간선수가 없는 노드들 구하고 시작
   
    while stack :
        node = stack.pop()
        answer.append(node)

        for i in range(len(graph[node])) : # 해당노드 인접 노드들 검사
            if graph[node][i] != 0 :
                in_degree[i] -= 1
                if  in_degree[i] == 0 : # 간선 -1 하고 0이면 바로 스택 append
                    stack.append(i)
    print(answer)

graph = [[0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]]

topological_sort(graph)


#########큐를 사용해서 같은 위상을 가진 정점은 배열로 묶어서 출력하기

def queue_topo (graph) :
    queue = [] #큐라고 썼지만 pop하지않아서 사실상 리스트를 통해 구현
    in_degree = [0]* len(graph) #초기화,, 인접리스트라?
    answer = []

    for i in range(len(graph)) :
        for j in range(len(graph)) :
            temp =  graph[j] 
            for k in range(len(temp)):
                if temp[k] == i : #길이 있을때
                    in_degree[i] += 1

    for i in range(len(in_degree)) :
        if in_degree[i] == 0 : queue.append(i)


    while queue :
        answer.append(queue) # 같은 위상을 가진 노드의 배열

        new_arr = []
        for i in queue : #i에서 탐색 - i는 노드 번호
            for j in range(len(graph[i])) :
                index = graph[i][j] 
                in_degree[index] -= 1 #연결노드가 있으면 연결 노드 차수 -1
                if in_degree[index] == 0 :
                    new_arr.append(index)
        
        queue = new_arr # 해당 레벨의 노드들을 저장

    for i in answer :
        print(i)


list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}

queue_topo(list)
