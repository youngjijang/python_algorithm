class Solution:
    def compress(self, chars: List[str]) -> int:
        result = ""
        count = 0
        for i in chars :
            if result == '' or result[-1] != i :
                if count > 1 :
                    result = result + str(count)
                result = result + i
                count = 1
            else :
                count += 1
        if count > 1 :
            result = result + str(count)
        # print(result)
        # chars = list(result)
        # print(chars)
        for i in range(len(result)) :
            chars[i] = result[i]
        chars = chars[:len(result)]

        return len(chars)