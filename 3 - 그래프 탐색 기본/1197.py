import sys
v,e = map(int,sys.stdin.readline().split())
p = [tuple(map(int,sys.stdin.readline().split())) for _ in range(e)]

p.sort(key=lambda x : x[2]) #!!!!!!!!작은 가중치 부터 선택해야하기때문에 정렬!!!!!!
# print(p)

parent = [i for i in range(v+1)]
sum = 0
#union find - 부모노드를 찾는 함수
def getParent(x) :
    if parent[x] == x : return x
    parent[x] = getParent(parent[x])
    return parent[x]

#union find - 부모 노드를 합치는 함수 
# 두 노드를 연결한다는 개념으로 이해
def unionParent(a,b) :
    a = getParent(a)
    b = getParent(b)
    if a < b : parent[b] = a
    else : parent[a] = b

#union find - 같은 부모를 가지는지 확인
def findParent(a,b) :
    a = getParent(a)
    b = getParent(b)
    if a == b : return 0 #같은 부모를 가지고있다. 즉 연결된 노드이다. 
    return 1

for i in p :
    if findParent(i[0],i[1]) != 0: # 연결 노드의 부모노드가 다르면 > 통일해주자
        unionParent(i[0],i[1]) 
        sum += i[2]
    # 부모노드가 같을 경우 이미 연결이 확인된거니까 pass


# print(parent)
print(sum)
    