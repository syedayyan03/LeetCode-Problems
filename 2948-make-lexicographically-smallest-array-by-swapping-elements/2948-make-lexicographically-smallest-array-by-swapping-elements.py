class Solution(object):

    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        arr = sorted((nums[i], i) for i in range(len(nums)))

        start = 0

        while start < len(nums):
            end = start
            while (end + 1 < len(nums) and
                   arr[end + 1][0] - arr[end][0] <= limit):
                end += 1
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            for i in range(start, end + 1):
                nums[indices[i - start]] = arr[i][0]

            start = end + 1

        return nums