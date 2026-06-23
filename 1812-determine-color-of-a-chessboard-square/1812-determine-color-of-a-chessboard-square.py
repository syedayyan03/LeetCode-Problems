class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        colIndex = 0
        rowIndex = 0
        
        for k in range(len(coordinates)):
            if coordinates[k] in columns:
                colIndex = columns.index(coordinates[k])
            elif coordinates[k] in rows:
                rowIndex = rows.index(coordinates[k])
            else:
                return False
        
        if colIndex % 2 == 0 and rowIndex % 2 == 0 or colIndex % 2 != 0 and rowIndex % 2 != 0:
            return False
        
        return True
        
                


        