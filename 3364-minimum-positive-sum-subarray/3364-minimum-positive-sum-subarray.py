class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            temp = []
            for j in range(i, min(i + r, len(nums))):
                temp.append(nums[j])
                if l <= len(temp) <= r:
                    s = sum(temp)
                    if s > 0:
                        ans = min(ans, s)

        return ans if ans != float('inf') else -1