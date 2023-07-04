class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        world = s.split(" ")
        ans = ""
        for i in world[::-1] :
            if i != "" : 
                ans = ans + i + " "
        return ans.strip()