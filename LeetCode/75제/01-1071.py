####### 내답안 - 거지같은 코드~

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2 : return str1

        ans = ''
        temp = ''
        a = len(str1)
        b = len(str2)

        for i in range(a // 2 + 1) :
            temp = temp + str1[i]
            if a % len(temp) != 0 : continue
            if b % len(temp) != 0 : continue
            if check(str1,temp) and check(str2,temp) :
                ans = temp
        
        return ans



def check(s, c) :
    l = len(c)
    r = 0
    if r > len(s) : return False
    while r < len(s) :
        if "".join(s[r : r+l]) != c : 
            return False
        r += l

    return True


###################  모범답안

# 두문자 모두 동일한 문자열의 반복일때 특징을 생각해보기
# 1. 두문자를 합쳤을때 동일해야한다. -> 이 로직이 이분법으로 구분된다는게 잘 떠오르지 않는다.
# 2. 반복 문자 중 가장 긴 문자열이기 때문에 두문자의 최대 공약수 길이와 동일하다

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       
        if str1 + str2 != str2 + str1:
            return ""

        from math import gcd
        return str1[:gcd(len(str1), len(str2))] # 최대공약수


################## 재귀

def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2 # 동일한 부분을 계속 잘라내고 마지막 남은 문자열 반환!!!
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1) # lengh가 긴 문자를 앞으로 하여 검증
        elif str1[: len(str2)] == str2: # 짧은 문자열을 기준으로 동일한 문자인지 파악하여 동일하지 않으면 false return
            return self.gcdOfStrings(str1[len(str2) :], str2) # 동일하다면 동일한 부분을 잘라서 재 비교
        else:
            return ''