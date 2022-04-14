import sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().split() for _ in range(n)]
#파이썬에서는 따로 스택 라이브러리가 존재하지않는다. 
# 보통 덱 라이브러리를 import해서 스택 대신사용한다.

#리스트 함수를 사용해서 간단하게 스택을 사용할수있다.
#stack은 배열(list) 혹은 연결리스트로 구현한ㄷ다.
stack = []

for i in a :
    m = i[0]
    if m == 'push' : stack.append(i[1])
    elif m == 'pop' : 
        print(-1 if len(stack)==0 else stack.pop())
    elif m == 'size' : print(len(stack))
    elif m == 'empty' :
        print(1 if len(stack)==0 else 0)
    else: 
        print(-1 if len(stack)==0 else stack[len(stack)-1])

        
