import sys

n,m = map(int,sys.stdin.readline().split())
p = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]

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

result = [] # 각 노드에 루트노드를 구해여 저장한다. 
for a in parent :
    result.append(getParent(a)) 


print(result)
print(set(result)) 
# 루트 노드에 중복을 제거하여 총 몇개의 루트가 남아있나 확인함으로 사이클의 개수를 알수있다. 

print(len(set(result))-1)
