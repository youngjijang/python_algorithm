import sys

all=[]
while 1 :
   t = input()
   if t == '0' :
        break
   else :
       n,*a = t.split()
       all.append(a)
# print(all)

# for i in range(len(all)) :
#     all[i] = list(all[i].split())

# print(all)

def rotto (n,c) :
    case = []
    if n == 0 :
        return [[]]
    for a in range(len(c)) :
        elem = c[a]
        for rest in rotto(n-1,c[a+1:]) :
            case.append([elem]+rest)
        # print(case)
    return case

for i in range(len(all)) :
    c = all[i] #테스트 케이스
    # c = c[1:]
    # for i in range(int(all[i][0])) :
    for i in rotto(6,c):
        print(*i)
    # rotto(3,c)
    if i != (len(all)-1) : print()