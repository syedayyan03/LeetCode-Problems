class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        rem = 1
        while(True):
            temp = n
            while(temp > 0):
                rem *= temp % 10
                temp //= 10
            if rem % t == 0:
                return n
            rem = 1
            n+= 1
        
        return n
        
        