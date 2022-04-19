# 인접 행렬
from collections import deque

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


#######################################
# 최단거리 구하기 (2차원 행렬)

m,n = 6,4
dx,dy = [1,-1,0,0],[0,0,1,-1]

def short(x,y,board,visited) :
    # 시작점도 이동 카운트로 치면 큐에 넣고, 아니면 0
    q = deque([(x,y,1)]) #x,y,거리
    visited[x][y] = True
    while q :
        cur = q.popleft() # 현재 값

        #목적지에 도달 - bfs는 현재가 항상 최적의 경로임을 보장한다. -??????
        if cur[0] == n-1 and cur[1] == m-1 : # 행렬 마지막 좌표
            print(cur[2]) # 경로 길이
            return 

        for i in range(4) :
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[0]
            if 0 <= xx <n and 0 <= yy < m and not visited[xx][yy] and board[xx][yy] == '1' :
                visited[xx][yy] = True
                q.append((xx,yy,cur[2]+1))

