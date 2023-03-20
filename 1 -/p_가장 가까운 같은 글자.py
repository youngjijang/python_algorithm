from collections import defaultdict
def solution(s):
    answer = []
    temp = defaultdict(int)
    for i in range(len(s)) :
        if temp[s[i]] == 0 :
            answer.append(-1)
        else :
            answer.append(i + 1 -temp[s[i]])
        temp[s[i]] = i + 1
    return answer