import sys

n,k = map(int,sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(n)]
x.sort()
# def sol() :
#     for i in range(n) :
start = min(x)
end =  max(x)+k

while start <= end :#!!!!!!!!!!!!!!11 헷갈림
    sum = 0
    mid = (start+end)//2
    for i in x :
        if mid > i :
            sum += (mid-i)
    if sum > k :
        end = mid - 1 
    else :
        start = mid + 1

print(end)#!!!!!!!!!!!!!!!