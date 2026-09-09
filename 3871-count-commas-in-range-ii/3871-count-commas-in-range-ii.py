class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        power = 1000

        while power <= n:
            total += n - power + 1
            power *= 1000

        return total