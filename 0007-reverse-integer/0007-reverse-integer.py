class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = abs(x)
        while num != 0:
            n = num%10
            num //= 10
            rev = rev*10 + n
        if rev > 2**31 -1:
            return 0
        if x > 0:
            return rev
        else:
            return -rev

        