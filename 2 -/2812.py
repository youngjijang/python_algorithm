import sys

n,k = map(int,sys.stdin.readline().split())
num = sys.stdin.readline().strip() #string으로 받아서 인덱스로 쪼개기

stack=[]
l = n-k
for i in range(n) :
    while k > 0 :
        if stack and stack[-1] < num[i] : 
            stack.pop()
            k -= 1
        else : break
    stack.append(num[i])

print(''.join(stack[:l]))
        
