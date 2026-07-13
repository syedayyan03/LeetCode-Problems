import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixcopy = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrixcopy[i][j] == 0:
                    row_index = i 
                    num_cols = len(matrix[row_index])
                    matrix[row_index] = [0] * num_cols

                    col_index = j 
                    for row in matrix:
                        row[col_index] = 0
                    

        