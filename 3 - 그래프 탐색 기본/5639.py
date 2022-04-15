import sys
sys.setrecursionlimit(10**7)

nums = []
while 1 :
    try :
        x = int(sys.stdin.readline().strip())
    except :
        break
    nums.append(x)

# 전위 순회 > 후위 순회

def sol(list) :
    if len(list) == 1 :
        print(list[0])
        return
    
    x = list[0]
    result = len(list)
    for i in range(1,len(list)) :
        if list[i] > x :
            result = i
            break

    if result != len(list) and result != 1 :
        sol(list[1:result])
        sol(list[result:])
        print(x)
    else : #한쪽 노드가 없을 경우
        sol(list[1:])
        print(x)

sol(nums)