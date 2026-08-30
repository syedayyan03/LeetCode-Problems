class Solution(object):
    def minimumDeletions(self, nums):
        minPos = nums.index(min(nums))
        maxPos = nums.index(max(nums))

        l = len(nums)

        if minPos >= l - minPos and maxPos >= l - maxPos:
            return l - min(minPos, maxPos)

        elif minPos < l - minPos and maxPos < l - maxPos:
            return max(minPos, maxPos) + 1

        elif minPos < l - minPos and maxPos > l - maxPos:
            return min(
                max(minPos, maxPos) + 1,
                l - min(minPos, maxPos),
                minPos + 1 + l - maxPos
            )

        else:
            return min(
                max(minPos, maxPos) + 1,
                l - min(minPos, maxPos),
                maxPos + 1 + l - minPos
            )