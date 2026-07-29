class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n-1
        while(start<end):
            mid = start + (end-start)//2
            if nums[mid+1] > nums[mid]:
                start = mid + 1
            else:
                end = mid

        return start
        
        
        