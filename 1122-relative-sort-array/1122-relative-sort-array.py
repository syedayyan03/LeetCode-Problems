class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        values = {}
        for i in range(len(arr1)):
            if arr1[i] not in values:
                values[arr1[i]] = 1
            else:
                values[arr1[i]] += 1
        ans = []
        for i in range(len(arr2)):
            times = values[arr2[i]]
            for j in range(times):
                ans.append(arr2[i])
        
        arr1.sort()
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                ans.append(arr1[i])
        
        return ans


        