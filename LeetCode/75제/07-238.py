class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        sub = []
        temp = 1
        for i in range(len(nums)) :
            temp *= nums[i]
            pre.append(temp)

        temp = 1
        for i in range(len(nums)-1, -1, -1) :
            temp *= nums[i]
            sub.append(temp)
        
        ans = []
        for i in range(len(nums)) :
            if i == 0 :
                ans.append(sub[len(nums)-i-2])
            elif i == len(nums) -1 :
                ans.append(pre[i-1])
            else :
                ans.append(pre[i-1] * sub[len(nums)-2-i])
        

        return ans 


########### 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1

        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out