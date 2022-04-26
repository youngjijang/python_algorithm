import sys


all = []
while 1 :
    a = list(map(int,sys.stdin.readline().split()))
    if a == [-1, -1,-1] :
        break
    all.append(a)

arr = [[[0]*21]*21]*21
arr[0][0][0] = 1

for a in range(1,21) :
    for b in range(1,21) :
        for c in range(1,21) :
            if a < b < c :
                arr[a][b][c] = arr[a][b][c-1] + arr[a][b-1][c-1] - arr[a][b-1][c]
            else :
                arr[a][b][c] = arr[a-1][b][c] + arr[a-1][b-1][c] + arr[a-1][b][c-1] - arr[a-1][b-1][c-1]

print(arr)

result = []
for i in all :
    a,b,c = i[0],i[1],i[2]
    if a <= 0 or b <= 0 or c <= 0 :
        result.append(arr[0][0][0])
    if a>20 or b>20 or c>20 :
        result.append(arr[20][20][20])
    else :
        result.append(arr[a][b][c])

print(result)



        


     