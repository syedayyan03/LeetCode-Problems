class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        strn = str(n)
        strx = str(x)
        if strn[0] == strx:
            return False
        if strx not in strn:
            return False
        
        return True

        