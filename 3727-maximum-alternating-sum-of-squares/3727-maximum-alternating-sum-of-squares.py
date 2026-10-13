class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        score = 0
        n = len(nums)
        for i in range(n):
            if i < n // 2:
                score -= nums[i] ** 2
            else:
                score += nums[i] ** 2
        return score
