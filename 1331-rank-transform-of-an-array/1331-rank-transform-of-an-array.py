class Solution:
    def arrayRankTransform(self, arr: List[int]):
        temp = arr.copy()
        temp.sort()

        pos = {}
        rank = 1

        for num in temp:
            if num not in pos:
                pos[num] = rank
                rank += 1

        ans = []
        for num in arr:
            ans.append(pos[num])

        return ans