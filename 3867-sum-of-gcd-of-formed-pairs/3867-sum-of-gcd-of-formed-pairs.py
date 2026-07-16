import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            gcd = math.gcd(maxi, nums[i])
            prefixGcd.append(gcd)
        
        prefixGcd.sort()
        
        ans = 0
        for i in range(0, n//2):
            ans += math.gcd(prefixGcd[i], prefixGcd[n-i-1])
        return ans    

        