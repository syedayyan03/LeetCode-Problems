class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = max(nums)
        secmax = 0
        for i in range(len(nums)):
            if nums.count(maximum) >= 2:
                return (maximum-1) ** 2
            elif nums[i] > secmax and nums[i] < maximum:
                secmax = nums[i]
        return (maximum-1)*(secmax-1)
        