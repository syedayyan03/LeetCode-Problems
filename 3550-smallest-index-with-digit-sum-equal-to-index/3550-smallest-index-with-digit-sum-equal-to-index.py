class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            rem = self.summation(nums[i])
            if rem == i:
                return i
        return -1
    
    def summation(self, num):
        rem = 0
        while(num > 0):
            rem += num % 10
            num //= 10
        return rem
        