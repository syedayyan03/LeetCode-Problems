class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        alldigits = []

        for i in range(len(digits)):
            l = mapping[digits[i]]
            alldigits.append(l)

        ans = [""]

        for i in range(len(alldigits)):
            temp = []
            for s in ans:
                for ch in alldigits[i]:
                    temp.append(s + ch)
            ans = temp

        return ans