import sys

n,c = map(int,sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(n)]

# start = min(x)
# end = max(x)
x.sort()
# 1. 집들 사이에 최대gap과 최소gap을 구한후 이분 탐색을 통해 적절한 gap을 구한다.
# 2. 해당 gap일때 공유기의 수가 c 이하면 gap을 줄이고 c이상이면 gap을 늘린다.
# 3. 공유가 수가 c인 경우의 gap중에 가장 큰 경우

start = 0
end = max(x) - min(x)
while start <= end :
    mid = (start+end)//2 #gap

    #x[0]부터 공유기1개에서 시작
    value = x[0]
    count = 1 
    # 해당 gap일때 공유기 최대 몇개들어가는지 확인
    for i in range(1,n) :
        if x[i] >= value + mid :
            value = x[i]
            count += 1

    # 공유기 수에 따라 start, end 변경히며 조절
    if count >= c :
        start = mid +1
        result = mid 
        #이부분이 헷갈린다. 어떤 경우에는 그냥 추출해도되고 어떤 경우에는 mid값이 변경되지않게 미리 저장해둬야한다.
        # 아마 최대값을 구하는 거라 그런거같긴한데,,,,, 공유기수가 c와 동일하다고 끝나는게 아니라 최대값인지 계속 확이하는 과정에서,,?
    else : end = mid - 1

print(result)

