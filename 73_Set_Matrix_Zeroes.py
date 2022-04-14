class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w, h = len(matrix[0]), len(matrix)
        visited = [[0] * w for _ in range(h)]
        
        
        def _turn_zeros(i, j):
            visited[i][j] = 1
            for ii in range(h):
                if matrix[ii][j] != 0:
                    visited[ii][j] = 1
                matrix[ii][j] = 0
            for jj in range(w):
                if matrix[i][jj] != 0:
                    visited[i][jj] = 1
                matrix[i][jj] = 0

        for i in range(h):
            for j in range(w):
                
                if visited[i][j] == 0 and matrix[i][j] == 0:
                    _turn_zeros(i, j)
