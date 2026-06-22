class Solution:
    def maxDistinct(self, s: str) -> int:
        chars = []
        for i in range(len(s)):
            if s[i] not in chars:
                chars.append(s[i])
            
        return len(chars)

        