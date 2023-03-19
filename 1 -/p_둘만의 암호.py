def solution(s, skip, index):
    a = 'abcdefghijklmnopqrstuvwxyz'
    a = list(a)
    answer = ''
    for i in skip :
        a.remove(i)
    for i in s :
        t = a.index(i)+index
        while t >= len(a) :
            t -= len(a)
        answer += a[t]
    return answer