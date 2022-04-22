import sys

n = int(sys.stdin.readline())

def fib3(n) :
    # if n == 1 :
    #     return 1
    a,b = 0,1
    for _ in range(n) :
        a %= 15746
        b %= 15746
        a,b = b, (a+b)%15746
    return b

#나머지 분배 법칙,,,,,,,,,,,

print(fib3(n))
