
n,b = map(int,input().split())
a = [[*map(int,input().split())] for _ in range(n)] #n개 줄로 받은 line을 쪼개서 int로 이차원 배열 저장

def cal(l,ll):
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n):  
            for k in range(n) :
                result[i][j] += l[i][k] * ll[k][j]
            result[i][j] %=1000

    return result #2차 배열

def multi(num) :
    if num == 1 : # 1000일 경우 생각하기
        for i in range(n) :
            for j in range(n) :
                if a[i][j] >= 1000 :
                    a[i][j] %= 1000
        return a
    temp = multi(num//2) # 2차배열
    if num%2 == 0 :
        result = cal(temp,temp)
    else :
        result = cal(a,cal(temp,temp))
    return result

result = multi(b)


for i in result :
    for j in i :
        print(j,end=' ')
    print()