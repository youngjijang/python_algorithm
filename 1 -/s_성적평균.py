import sys

N,K = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
for _ in range(K) :
    a,b = map(int, sys.stdin.readline().split())
    l = score[a-1:b]
    print(format(sum(l)/len(l),".2f"))