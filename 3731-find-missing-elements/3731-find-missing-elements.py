class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if len(nums) >= 2:
            mini = min(nums)
            maxi = max(nums)
        
        setting = []
        for i in range(mini, maxi):
            setting.append(i)
        
        ans = []
        for i in range(len(setting)):
            if setting[i] not in nums:
                ans.append(setting[i])
        
        return ans


        