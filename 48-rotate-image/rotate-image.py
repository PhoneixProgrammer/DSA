class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        #  1    2    3             1  4  7       7  4  1
        #  4    5    6      ---->  2  5  8  -->  8  5  2
        #  7    8     9            3  6   9      9  6  3

        # Transpose of the matrix -- > O(n^2)
        for i in range(n): #i = 0
            for j in range(i+1,n) : 
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for row in matrix : # O(n^2)
            row.reverse()
        
        #Optimal Time Complexity :
        #Total Time complexity : O(n^2)

