class Solution:
    def maxProduct(self, n: int) -> int:
        ans = 1
        nums = []
        while(n > 0):
            ans = n % 10
            n //= 10
            nums.append(ans)
        
        nums.sort()    
        ans = nums[-1] * nums[-2]
        return ans

        