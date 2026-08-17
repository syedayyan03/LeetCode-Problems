class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for i in range(len(strs)):
            word = []

            for j in range(len(strs[i])):
                word.append(strs[i][j])

            word.sort()
            key = ''.join(word)

            if key not in words:
                words[key] = []

            words[key].append(strs[i])

        return list(words.values())