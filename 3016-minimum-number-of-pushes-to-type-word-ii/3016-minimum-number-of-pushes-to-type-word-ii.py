class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        freq = {}

        for char in word:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        setting = set()
        for char in word:
            setting.add(char)

        setting = list(setting)

        setting.sort(key=lambda char: freq[char], reverse=True)
        for i in range(len(setting)):
            pushes += ((i // 8) + 1) * freq[setting[i]]
        
        return pushes

        