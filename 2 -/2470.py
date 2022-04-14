import sys

n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
x.sort()

def tozero() :
    start = 0
    end = len(x)-1
    result = (x[start],x[end],abs(x[start]+x[end]))
    while start < end :
        A = x[start]
        B = x[end]
        if abs(A+B) < result[2] :
            result=(A,B,abs(A+B))
        if A + B == 0 :
            break
        if A + B < 0 :
            start += 1
        else :
            end -= 1
    return result

result = tozero()
print(result[0],result[1])


