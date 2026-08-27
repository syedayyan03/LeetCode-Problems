class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                ans = min(ans, n - dist, dist)

        return -1 if ans == n else ans