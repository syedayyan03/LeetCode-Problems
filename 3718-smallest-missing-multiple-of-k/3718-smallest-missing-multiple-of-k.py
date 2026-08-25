class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while(True):
            if k * i in nums:
                i += 1
            else:
                return k * i
        
        