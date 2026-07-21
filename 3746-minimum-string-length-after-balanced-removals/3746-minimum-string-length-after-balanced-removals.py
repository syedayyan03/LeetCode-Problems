class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        counta = s.count('a')
        countb = s.count('b')

        return abs(counta - countb)
        