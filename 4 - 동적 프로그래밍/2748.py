
import sys

n = int(sys.stdin.readline())

####시간 초과######3걍 재귀함수 ,dp  XX
def fib (n) :
    array = [0,1]
    if len(array) > n :
        return array[n]
    else :
        result = fib(n-1) + fib(n-2)
        array.append(result)
        return result

#####################3
# 공간복잡도?
def fib2 (n) :
    if n == 0 : return 0
    elif n == 1 : return 1
    array=[0,1]

    for i in range(2,n+1) :
        num = array[i-1] + array[i-2]
        array.append(num)

    return array[n]

#################### O(n) > 피보나치 수열이 아닌 '수'를 구할때만 효율적
def fib3(n) :
    if n <=2 :
        return 1
    a,b = 0,1
    for x in range(n-1) :
        a,b = b, a+b
    return b

###########공식 이용하기 - 2747통과/2748 틀렸습니다. 정확도가 80정도부터 떨어지는듯
def fib4(n) :
    root5 = pow(5,0.5)
    ratio = (1+root5)/2
    return int((pow(ratio,n) - pow(1-ratio,n))/root5)

print(fib2(n))