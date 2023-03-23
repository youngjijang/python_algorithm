def solution(number, k):
    stack = []
    for i in number :
        while stack and stack[-1] < i and k:
            stack.pop()
            k -= 1
        if len(stack) < len(number)-k :
            stack.append(i) 
    return ''.join(stack)