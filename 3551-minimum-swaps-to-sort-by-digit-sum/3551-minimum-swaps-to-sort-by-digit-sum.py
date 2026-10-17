from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        n = len(nums)
        arr = [(digit_sum(num), num, i) for i, num in enumerate(nums)]
        arr.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps