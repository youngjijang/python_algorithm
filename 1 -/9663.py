import sys

n = int(sys.stdin.readline())

isused = [False] * n #isused[행] = [] 
isused2 = [False]*(2*n-1) #상승 대각선 - [y+x] 
isused3 = [False]*(2*n-1) #하강 대각선 - y

# print(isused2)
queen = []
count = 0

def check(x) :
    global count
    if x == 0 :
        count += 1
        # print(queen)
    else :
        for i in range(n) :
            if isused[i] == False :
                isused[i] = True
                isused2[i+queen[i]] = True
                isused3[i-queen[i]+(n-1)] = True
                for j in range(2*n-1) :
                    if isused2[j] == False :
                        for z in range(2*n-1) :
                            if isused3[z] == False :
                                queen.append(i)
                                check(x-1)
                                queen.pop()
                                isused3[z] = False
                        isused2[j] = True
                isused[i] = False

check(n)
print(count)