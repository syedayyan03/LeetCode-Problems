class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp.append(matrix[i][j])
        
        temp.sort()
        return temp[k-1]

        