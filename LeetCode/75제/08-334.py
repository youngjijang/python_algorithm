### 삼중 반복문 ㅇㄸ
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if min(nums) + 2 > max(nums) : return False
        
        for i in range(len(nums)-2) :
            first = nums[i]
            for j in range(i+1,len(nums)-1) :
                if nums[j] <= first : continue
                second = nums[j]
                for k in range(j+1,len(nums)):
                    if nums[k] <= second : continue
                    return True
        return False

###### O(1)
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first, second = inf, inf
        
        for third in nums:
            
            if second < third: return True
            if third <= first: first= third    
            else:  second = third 
                
        return  False
