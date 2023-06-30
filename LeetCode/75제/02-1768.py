class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        a = len(word1)
        b = len(word2)
        maxi = max(a, b)
        for i in range (maxi) :
            if i < a :
                result = result + word1[i]
            if i < b :
                result = result + word2[i]

        return result