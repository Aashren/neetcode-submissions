class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(0,9):
            for y in range(0,9):
                temp=0
                if board[x][y] == ".":
                    continue
                while (temp<9):
                    if board[x][temp]==board[x][y] and temp!=y:
                        return False
                    temp+=1
        for x in range(0,9):
            for y in range(0,9):
                temp=0
                if board[y][x] == ".":
                    continue
                while(temp<9):
                    if board[temp][x]==board[y][x] and temp!=y:
                        return False
                    temp+=1
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                # Compare every cell with every other cell in the box
                for r1 in range(start_row, start_row + 3):
                    for c1 in range(start_col, start_col + 3):

                        if board[r1][c1] == ".":
                            continue

                        for r2 in range(start_row, start_row + 3):
                            for c2 in range(start_col, start_col + 3):

                                if (r1 != r2 or c1 != c2) and board[r1][c1] == board[r2][c2]:
                                    return False
        return True




            
        
                
            