import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()
# print(m_list)

def binary_serch(a) :
    st = 0
    en = n-1
    while st <= en :
        mid = (en+st)//2
        if n_list[mid] == a :
            return True
        elif n_list[mid] > a :
            en = mid -1
        else :
            st = mid + 1
    return False
        

for i in range(m) :
    # print(m_list[i])
    if binary_serch(m_list[i]) : print(1)
    else : print(0)

# 2차배열 중복 제거 해보기
# lst = [[1,2], [1,2], [1]]
# print(list(set(map(tuple,lst))))