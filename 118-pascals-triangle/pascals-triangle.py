class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for row in range(numRows):
            if row == 0:
                triangle.append([1])
            else : 
                # prev_row takes the last row that has been added to the triangle
                # because to build the current row because each number depends on the 2 numbers above it 
                prev_row = triangle[-1]
                current_row = [1]

                for i in range(1,len(prev_row)):
                    current_row.append(prev_row[i-1]+prev_row[i])
                current_row.append(1)
                triangle.append(current_row)
        return triangle

        # Solution 1:TimeComplexity is O(n2); n-->numRows
            