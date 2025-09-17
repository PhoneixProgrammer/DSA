class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #edge cases
        if not board or not board[0]:
            return 
        
        m, n  = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r >=m or c < 0 or c >=n or board[r][c]!='O':
                return 
            board[r][c] = 'S'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        #step 1: mark border connected 'O's
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        #step 2: flip 
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        #time complexity : O(mxn)
        #space complexity : O(mxn) --> recursive DFS
