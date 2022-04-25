import sys

n,k = map(int,sys.stdin.readline().split())
elec = list(sys.stdin.readline().split())

temp = []

for i in elec :
    if i not in temp :
        temp.append(i)
    if len(temp) == n : break
# print(temp)
count = 0
for i in range(n-1,k) : 
    if elec[i] in temp :
        continue
    count += 1
    re_temp = []
    for j in range(i+1,k) :
        if len(re_temp) == n -1 : break ##조건문 먼저 안해주면 n=1일때 반례
        if elec[j] in temp and elec[j] not in re_temp:
            re_temp.append(elec[j])
        
    temp = re_temp
    temp.append(elec[i])
    # print(temp)

print(count)

