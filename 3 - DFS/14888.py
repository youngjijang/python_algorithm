
import sys

n = int(sys.stdin.readline()) # 수열 수
A = list(map(int,sys.stdin.readline().split())) # 숫자 수열
o = list(map(int,sys.stdin.readline().split())) # 연산자
operator = []
for i in range(4) :
    for _ in range(o[i]) :
        operator.append(i)

print(operator)

def cal(x,y,oper) :
    if oper == 0 :
        return x + y
    elif oper == 1 :
        return x - y
    elif oper == 2 :
        return x*y
    elif oper == 3 :
        if x < 0 : return (-1*x//y) * -1
        return x//y

# minimum = 10**9 
# maximum = -10**9

def ans(arr,oper) :
    temp = arr[0]
    for i in range(n-1) :
        temp = cal(temp,arr[i+1],oper[i]) 

    return temp

answer = [] # 연산 결과를 담을 배열

stack = [-1] * (n-1) # 선택된 연산자 담기
seen = [False] * (n-1) #방문한 연산자인지 확인 / 인덱스 값이 연산자
def back(v): #v는 시작 
    if v == n-1 :
        # print(stack)
        # print(A)
        answer.append(ans(A,stack))
    else :
        for i in range(n-1):
            if not seen[i]:
                stack[v] = operator[i]
                # stack.append(operator[i])
                seen[i] = True
                back(v+1)
                stack[v] = -1
                # stack.pop()
                seen[i] = False
 
back(0)
print(max(answer))
print(min(answer))
