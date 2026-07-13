# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> list[int]:
#         ans = []
        
#         all_sequential = [
#             12, 23, 34, 45, 56, 67, 78, 89, 
#             123, 234, 345, 456, 567, 678, 789, 
#             1234, 2345, 3456, 4567, 5678, 6789, 
#             12345, 23456, 34567, 45678, 56789, 
#             123456, 234567, 345678, 456789, 
#             1234567, 2345678, 3456789, 
#             12345678, 23456789, 
#             123456789
#         ]
        
#         for i in all_sequential:
#             if low <= i <= high:
#                 ans.append(i)
        
#         return ans


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        sample = "123456789"
        
        all_sequential = []
        for length in range(2, 10):
            for start in range(10 - length):
                all_sequential.append(int(sample[start : start + length]))
        
        for i in all_sequential:
            if low <= i <= high:
                ans.append(i)
                
        return ans
