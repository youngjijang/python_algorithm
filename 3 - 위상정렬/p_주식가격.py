from collections import deque

## 유효성 미 통과
def solution(prices):
    answer = []
    que = deque(prices)
    while que :
        n = que.popleft()
        a = 1
        if not que : answer.append(0)
        elif que and n <= min(que) : 
            answer.append(len(que))
        else :
            for j in que :
                if j < n : 
                    break
                a += 1
            answer.append(a)
    return answer