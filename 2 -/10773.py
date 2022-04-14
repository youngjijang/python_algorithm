
import sys
k = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(k)]

result = []
for i in num :
    if i == 0 :
        result.pop()
    else : result.append(i)

print(sum(result))