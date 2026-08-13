class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(r, c):
            cnt = 0
            for i in range(max(0, r - 1), min(len(board), r + 2)):
                for j in range(max(0, c - 1), min(len(board[0]), c + 2)):
                    cnt += board[i][j]

            return cnt - board[r][c]
        
        res = [[0] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                ones = count(i, j)
                if board[i][j] == 1:
                    if ones in range(2, 4):
                        res[i][j] = 1
                else:
                    if ones == 3:
                        res[i][j] = 1
        
        board[:] = res
        
                    
                        