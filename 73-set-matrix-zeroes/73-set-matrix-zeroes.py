class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True
                    
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
            
        
        """
        Do not return anything, modify matrix in-place instead.
        """
#         inplace- no extra array or data structure will be added we must modify the given matrix or array


        