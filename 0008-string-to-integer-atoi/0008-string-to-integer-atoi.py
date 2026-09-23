class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        ans = ""
        count = 0
        if len(s) == 0:
            return 0

        if s[0] == "-":
            s = s[1:len(s)]
            count = 1
        elif s[0] == "+":
            s = s[1:len(s)]

        for i in range(len(s)):
            if s[i].isdigit():
                ans += s[i]
            else:
                break

        if ans == "":
            return 0

        num = 0

        for ch in ans:
            num = num * 10 + (ord(ch) - ord('0'))

        if count == 1:
            num = -num

        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num