import sys

n,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
trees.sort()
start = 0
end = trees[-1]

def sol(taget):
    sum = 0
    for i in trees :
        if i > taget :
            sum += (i-taget)
    if sum >= m : return True
    return False


while start < end :
    mid = (start+end)//2
    if sol(mid) :
        start = mid + 1
        result = mid
    else :
        end = mid

print(result)