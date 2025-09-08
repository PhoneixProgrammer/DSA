class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        #STEP 1: TRANSPOSE OF MATRIX( SWIPE ACROSS DIAGONAL)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #STEP 2: REVERSE EACH ROW
        for row in matrix:
            row.reverse()
