import sys

n,k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
for i in range(n-1,-1,-1) :
    ####시간초과
    # while a[i] <= k :
    #     k = k-a[i]
    #     count += 1
    if a[i] <= k :
        count += k // a[i]
        k = k % a[i]

print(count)
