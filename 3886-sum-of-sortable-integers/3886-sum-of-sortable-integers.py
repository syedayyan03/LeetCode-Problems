class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        pref_max = [0] * (n + 1)
        suff_min = [float('inf')] * (n + 1)
        pref_drop = [0] * n

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (nums[i - 1] > nums[i])

        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                end = start + k - 1

                drops = pref_drop[end] - pref_drop[start]

                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1 or pref_max[start] > suff_min[start]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans