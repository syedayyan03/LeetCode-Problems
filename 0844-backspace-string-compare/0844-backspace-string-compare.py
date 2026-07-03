class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = ""
        str2 = ""
        for i in range(len(s)):
            if s[i] == '#' and len(str1) > 0:
                str1 = str1[:-1]
            elif s[i] != '#':
                str1 += s[i]
        
        for i in range(len(t)):
            if t[i] == '#' and len(str2) > 0:
                str2 = str2[:-1]
            elif t[i] != '#':
                str2 += t[i]
        
        return str1 == str2
