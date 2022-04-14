# 괄호

import sys

t = int(sys.stdin.readline())
case = list(sys.stdin.readline().strip() for _ in range(t))

# print(case)
#stack에 저장안하고 그냥 문자열 비교로 했는데 이게 맞는지 몰겠음
#stack으로 어케 풀어?
def sol(i) :
    count = 0
    for j in i :
        if j == '(' : count += 1
        else : count -= 1
        if count < 0 : 
            return 'NO'
    if count == 0 : return "YES"
    return "NO"
        
for i in case :
    print(sol(i))