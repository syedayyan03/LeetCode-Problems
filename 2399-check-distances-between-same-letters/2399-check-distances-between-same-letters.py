class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        count = 0

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dis = j - i - 1
                    char = ord(s[i]) - ord('a')   
                    if distance[char] == dis:
                        count += 2

        return count == len(s)