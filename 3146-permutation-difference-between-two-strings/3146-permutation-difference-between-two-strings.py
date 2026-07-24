class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i] in t:
                index = t.index(s[i])
                ans += abs(i-index)
        
        return ans

        