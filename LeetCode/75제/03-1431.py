class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies)
        # print(greatest)
        for i in candies :
            if i + extraCandies >= greatest :
                result.append(True)
            else :
                result.append(False)
        return result