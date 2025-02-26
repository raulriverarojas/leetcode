import copy
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        def liveSurvives(board, row, col) -> int:
            dead=0
            live=0
            for rowi in range(max(0,row-1),min(MAX_ROW, row+2), 1):
                for coli in range(max(0, col-1), min(MAX_COL, col+2),1):
                    if rowi==row and coli==col:
                         continue
                    if board[rowi][coli]==1:
                        live+=1
                        if live>3:
                            return 0
                    else: 
                        dead+=1
                        if dead>6:
                            return 0
            
            if live>=2 and live<=3:
                return 1
            return 0

        def deadRevives(board, row, col) -> int:
            live=0
            for rowi in range(max(0,row-1),min(MAX_ROW, row+2), 1):
                for coli in range(max(0, col-1), min(MAX_COL, col+2),1):
                    if rowi==row and coli==col:
                         continue
                    if board[rowi][coli]==1:
                        live+=1
            if live==3:
                return 1
            return 0
        updatedBoard = copy.deepcopy(board)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]==1:
                    updatedBoard[row][col] = liveSurvives(board, row, col)
                else:
                    updatedBoard[row][col] = deadRevives(board, row, col)
        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] = updatedBoard[row][col]
        
if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    output = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    print("Expected out")
    print(output)
    solution = Solution()
    Solution.gameOfLife(solution, board)
    assert board == output

