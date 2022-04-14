
# 순열 : 순서 상관있음 - 모든 경우의 배열를 다 담음
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result

print(permutation([0,1,2,3], 2))

# 조합 : 순서 상관없음
def combination(arr, n):
    result = [] # 함수안에 있으면 호출될때마다 계속 초기화 되는게 아닌가?? 맞는듯
    if n == 0:
        return [[]] #왜 여기서 이중배열 - 빈 배열을 보내야 값엔 변화가없고 반복문을 한번 실행함
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest) 
    return result

print(combination([0,1,2,3], 2))

# print([5,0]-[0])

# one = []
# for i in [] :
#     one.append([0]+i)

# print(one)