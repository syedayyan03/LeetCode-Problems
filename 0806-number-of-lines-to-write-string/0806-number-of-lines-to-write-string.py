class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        currentWidth = 0

        for i in range(len(s)):
            wordval = ord(s[i]) - ord('a')

            if currentWidth + widths[wordval] > 100:
                lines += 1
                currentWidth = widths[wordval]
            else:
                currentWidth += widths[wordval]

        return [lines, currentWidth]