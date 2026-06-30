class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '|':
                count += 1
            
            if count %2 == 0:
                if s[i] == "*":
                    ans += 1
        
        return ans

        