class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans = 0
        diff = 0

        for ch in s:
            if ch == '1':
                diff += 1
            else:
                diff -= 1

            if abs(diff) <= 1:
                ans += 1

        return ans
        