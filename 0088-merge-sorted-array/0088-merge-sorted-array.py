class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3 = []

        for i in range(m):
            nums3.append(nums1[i])

        for j in range(n):
            nums3.append(nums2[j])

        nums3.sort()

        for i in range(m + n):
            nums1[i] = nums3[i]