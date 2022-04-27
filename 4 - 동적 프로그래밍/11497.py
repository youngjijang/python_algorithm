from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    n = int(sys.stdin.readline())
    namo = list(map(int,sys.stdin.readline().split()))

    namo.sort()
    
    result = deque([namo[0]])
    for i in range(1,n) :
        if i%2 == 0 :
            result.append(namo[i])
        else:
            result.appendleft(namo[i])

    level = abs(result[0]-result[n-1])
    for i in range(n-1) :
       if abs(result[i]-result[i+1]) > level :
           level = abs(result[i]-result[i+1])
    print(level)
