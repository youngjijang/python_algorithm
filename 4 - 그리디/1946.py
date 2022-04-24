import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    p = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    p.sort()
    # result = [True] * n
    # for i in range(n-1) :
    #     if result[i] == True :
    #         for j in range(i+1,n) :
    #             if p[i][1] < p[j][1] :
    #                 result[j] = False

    # print(result.count(True))

    #for문 돌리면 당연시간초과ㅠㅜㅜㅜㅜ
    #비교 대상만 temp에 담고 업데이트해 나아가기....중요중요
    count = 1
    temp = p[0][1]
    for i in range(1,n) :
        if p[i][1] < temp :
            count += 1
            temp = p[i][1]
    print(count)