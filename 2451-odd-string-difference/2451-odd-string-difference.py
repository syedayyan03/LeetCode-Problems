class Solution:
    def oddString(self, words: List[str]) -> str:
        groups = {}
        
        for word in words:
            temp = []
            for i in range(1, len(word)):
                diff = (ord(word[i]) - ord('a')) - (ord(word[i-1]) - ord('a'))
                temp.append(diff)
            pattern = tuple(temp)
            if pattern not in groups:
                groups[pattern] = []
            groups[pattern].append(word)        
        for pattern, word_list in groups.items():
            if len(word_list) == 1:
                return word_list[0]
