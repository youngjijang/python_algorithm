x,z,y = map(int,input().split())

# while 1 :
#     t = z//2
#     temp = x**t
#     if z%2 == 0 :
#         ((temp%y)*(temp%y))%y
#     else :
#        ((temp%y)*(temp%y)*(x%y))%y

def sol(n) :
    global x,y
    if n == 1 :
        return x%y
    temp = sol(n//2) 
    if n%2 == 0 :
        return ((temp%y)*(temp%y))%y
    else :
        return ((temp%y)*(temp%y)*(x%y))%y

print(sol(z))
