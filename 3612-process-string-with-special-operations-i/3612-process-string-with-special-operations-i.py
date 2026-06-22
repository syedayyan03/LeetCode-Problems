class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for char in s:
            if char == "#":
                if len(ans) != 0:
                    ans *= 2
            elif char == '*':
                if len(ans) != 0:
                    ans = ans[:-1]
            elif char == '%':
                if len(ans) != 0:
                    ans = ans[::-1]
            else:
                ans += char
        return ans

        