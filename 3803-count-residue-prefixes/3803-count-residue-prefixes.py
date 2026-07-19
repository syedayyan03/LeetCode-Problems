class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        ans = 0

        for i in range(len(s)):
            seen.add(s[i])

            if len(seen) == (i + 1) % 3:
                ans += 1

        return ans