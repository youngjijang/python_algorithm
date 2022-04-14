import sys

# 1. 각 번호에서 출발하여 제자리로 돌아오는 값을 구한다. 
# 2. 1번 과정을 반복하면서 최솟값을 업데이트한다. 

N = int(input())
travel = [list(map(int, input().split())) for _ in range(N)]

min_value = sys.maxsize
# min_value 보다 이미 값이 큰 경우는 무시하는 것이 빠르게 결과에 도출된다. 

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0: #시작 점으로 돌아가는 길
            min_value = min(min_value, value + travel[next][start])
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop() #마지막값을 


# # 각 번호에서 시작
# for i in range(N):
    #dfs(i,i,0,[i])
dfs(0, 0, 0, [0])

print(min_value)