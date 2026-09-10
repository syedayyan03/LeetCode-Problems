class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        cycle = 2 * numRows - 2
        ans = ""

        for row in range(numRows):

            i = row

            while i < len(s):

                ans += s[i]

                if row != 0 and row != numRows - 1:
                    diagonal = i + cycle - 2 * row

                    if diagonal < len(s):
                        ans += s[diagonal]

                i += cycle

        return ans