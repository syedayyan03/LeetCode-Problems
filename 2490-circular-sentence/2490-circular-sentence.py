class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i in range(len(words)):
            current = words[i]
            next_word = words[(i + 1) % len(words)]

            if current[-1] != next_word[0]:
                return False

        return True