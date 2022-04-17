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
    if len(list) == 1 : # 종료 조건 > 리스트가 하나 남았을때 자기자신 출력
        print(list[0])
        return
    
    x = list[0] # 노드
    result = len(list) #커트라인 - 초기값은 리스트 마지막
    for i in range(1,len(list)) :
        if list[i] > x : # 교차되는 순간부터 오른쪽 자식
            result = i
            break

    if result != len(list) and result != 1 : # 자식 노드가 2개일때
        sol(list[1:result])
        sol(list[result:])
        print(x)

    else : #한쪽 노드가 없을 경우
        sol(list[1:])
        print(x)

sol(nums)