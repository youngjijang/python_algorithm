import sys

n,m = map(int,sys.stdin.readline().split())
p = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
# p.sort()

parent = [i for i in range(n+1)]

#union find - 부모노드를 찾는 함수
def getParent(x) :
    if parent[x] == x : return x
    parent[x] = getParent(parent[x])
    return parent[x]

#union find - 부모 노드를 합치는 함수
def unionParent(a,b) :
    a = getParent(a)
    b = getParent(b)
    if a < b : parent[b] = a
    else : parent[a] = b

#union find - 같은 부모를 가지는지 확인
def findParent(a,b) :
    a = getParent(a)
    b = getParent(b)
    if a == b : return 0
    return 1

for i in p :
    if findParent(i[0],i[1]) != 0:
        unionParent(i[0],i[1])
        # unionParent(i[1],i[0]) 이거,,,,,,,,,,,,왜악

result = []
for a in parent :
    result.append(getParent(a))


print(result)
print(set(result))

print(len(set(result))-1)
