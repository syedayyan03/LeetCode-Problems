class Solution:
    def secondHighest(self, s: str) -> int:
        ans = set()
        for i in range(len(s)):
            if s[i].isdigit() and s[i] not in ans:
                ans.add(s[i])
        
        ans = list(ans)
        ans.sort()

        if len(ans) < 2:
            return -1
        return int(ans[-2])

        