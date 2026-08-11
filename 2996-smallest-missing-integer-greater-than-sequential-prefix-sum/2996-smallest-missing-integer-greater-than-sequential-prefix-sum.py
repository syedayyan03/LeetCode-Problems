class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                ans += nums[i]

            else:
                break

        while True:
            if ans in nums:
                ans += 1
            else:
                break

        return ans