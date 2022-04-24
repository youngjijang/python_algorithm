import sys

n = int(sys.stdin.readline())
i = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#회의실 한개?
i.sort(key=lambda x : (x[1],x[0]))
result = [i[0]]
for j in range(1,n) :
    if i[j][0] >= result[-1][1] :
        result.append(i[j])
        
print(len(result))