class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','A','E','I','O','u','U']
        stack = []
        for i in s :
            if i in vowels :
                stack.append(i)

        print(stack)
        
        s = list(s)
        for i in range(len(s)) :
            if s[i] in vowels :
                s[i] = stack.pop()

        return ''.join(s)