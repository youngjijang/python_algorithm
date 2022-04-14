import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = [input() for _ in range(n)]

isused = [False] * n
results = []

def chose(a,result) :
    if a == k :
        result = int(result)
        if result not in results :
            results.append(result)
    else :
        for i in range(n) :
            if isused[i] == False :
                isused[i] = True
                result2 = result + nums[i] 
                chose(a+1, result2)
                isused[i] = False


chose(0,'')
# print(results)
print(len(results))
