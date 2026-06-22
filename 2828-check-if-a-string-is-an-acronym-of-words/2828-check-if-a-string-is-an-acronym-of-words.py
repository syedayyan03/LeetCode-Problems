class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        count = 0
        for i in range(len(s)):
            if s[i] == words[i][0]:
                count += 1
        
        if count == len(s):
            return True
        return False
        