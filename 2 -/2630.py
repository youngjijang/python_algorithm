import sys

n = int(input())
paper = [input().split() for _ in range(n)]

# print(paper)
white = 0
blue = 0

def sol(x,y,n) :
    c = paper[x][y]
    # print(c)
    for i in range(n) :
        for j in range(n) :
            if paper[x+i][y+j] != c : return False
    return True
def colorparper(n,x,y) : 
    global white,blue
    if sol(x,y,n) : 
        if paper[x][y] == '1' : blue += 1
        else : white += 1
    else :
        if n == 1 : return
        t = n//2
        colorparper(t,x,y)
        colorparper(t,x+t,y)

        colorparper(t,x,y+t)
        colorparper(t,x+t,y+t)

colorparper(n,0,0)
print(white)
print(blue)
