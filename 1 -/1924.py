import sys

x,y = map(int,sys.stdin.readline().split())

week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
mouth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = 0

# for i in range(2,int(x)+1) :
#     if (i-1) in [1,3,5,7,8,10,12] :
#         day += 31
#     elif (i-1) in [4,6,9,11] :
#         day += 30
#     elif (i-1) == 2 :
#         day += 28


# day += (int(y)-1)
for i in range(x) :
    day += mouth[i]
day += y
print(week[day%7])