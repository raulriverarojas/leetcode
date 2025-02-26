class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        # a dictionary for each row, col and 9 area
        # loop over each element and add it to the corresponding row, col and area dicts
        
        # areas = [[{},{},{}] for x in range(3)]
        areas = [[{},{},{}],[{},{},{}],[{},{},{}]]
        rows = [{},{},{},{},{},{},{},{},{}] 
        # rows = [{} for rows in range(n)]
        cols = [{},{},{},{},{},{},{},{},{}] 
        # cols = [{} for cols in range(n)]
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]!=".":
                    if cols[col].get(board[row][col], -1)!=-1 or rows[row].get(board[row][col], -1)!=-1 or areas[row//3][col//3].get(board[row][col], -1)!=-1:
                        return False
                    cols[col][board[row][col]]=board[row][col]
                    rows[row][board[row][col]]=board[row][col]
                    areas[row//3][col//3][board[row][col]]=board[row][col]
        return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    result= True
    solution = Solution()
    returned = Solution.isValidSudoku(solution, board)
    assert result == returned
