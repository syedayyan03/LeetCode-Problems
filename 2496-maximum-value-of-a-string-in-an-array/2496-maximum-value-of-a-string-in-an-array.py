class Solution(object):
    def maximumValue(self, strs):
        max_val = 0

        for s in strs:
            if s.isdigit():
                value = int(s)
            else:
                value = len(s)

            max_val = max(max_val, value)

        return max_val