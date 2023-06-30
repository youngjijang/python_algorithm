class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = False
        for i in range(len(flowerbed)) :
            if flowerbed[i] == 0 :
                if i == 0 or flowerbed[i-1] == 0 :
                     if i == len(flowerbed)-1 or flowerbed[i+1] == 0 :
                        n -= 1
                        flowerbed[i] = 1
            if n <= 0 :
                result = True
                break
        return result