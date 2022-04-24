import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    p = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    # for i in range(n) :
    #     if p[i][0] == 1 :
    #         one = p[i][1]
    #         print(one)
    #     if p[i][1] == 1 :
    #         two = p[i][0]
    #         print(two)
    # count = 0
    # for i in range(n) :
    #     temp = p[i]
    #     if one >= temp[1] and two >= temp[0] :
    #         print(temp)
    #         count += 1
    # print(count)

    p.sort()
    
    result = []
    result.append(p[0])
    for i in range(1,n) :
        if p[i][1] < p[0][1] :
            result.append(p[i])
    
    print(result)

    result.sort(key= lambda x : x[1])

    result2 = []
    result2.append(result[0])
    for i in range(1,len(result)) :
        if result[i][0] < result[0][0] :
            result2.append(result[i])

    print(result2)
    print(len(result2))
