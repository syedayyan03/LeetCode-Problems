class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        if min(nums1) % 2 == 1:
            return True

        return all(x % 2 == 0 for x in nums1)