class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        startIndex = s.find(goal[0])

        while startIndex != -1:   

            index = 0

            for i in range(startIndex, len(s)):
                if s[i] != goal[index]:
                    break
                index += 1
            else:
                for i in range(startIndex):
                    if s[i] != goal[index]:
                        break
                    index += 1
                else:
                    return True

            startIndex = s.find(goal[0], startIndex + 1)  

        return False