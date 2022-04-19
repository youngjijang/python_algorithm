from collections import deque
import sys

n,k = map(int,sys.stdin.readline().split())

visited = [0] * 100001
q = deque([])

visited[n] = 1
q.append((n,0))


while q :
    cur = q.popleft()
    if cur[0] == k :
        print(cur[1])
        exit(0)
    
    for i in [cur[0]+1, cur[0]-1, cur[0]*2] :
        if 0 <= i < 100001 and visited[i] == 0 :
            visited[i] = 1
            q.append((i,cur[1]+1))


# visited = [0] * 100001
# q = deque([])

# visited[n] = 1
# q.append(n)

# while q:
#     cur = q.popleft()
#     if cur == k:
#         print(visited[cur] - 1)

#     for i in [cur + 1, cur - 1, cur * 2]:
#         if 0 <= i < 100001 and visited[i] == 0:
#             visited[i] = visited[cur] + 1
#             q.append(i)