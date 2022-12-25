class Sudokuboard:
    
    def __init__(self):
        self.board = [[0] * 9 for _ in range (9)]

    def print_board(self, highlight_row=-1):
        for r, row in enumerate(self.board):
            if highlight_row == r:
                print(f"> Row# {r+1}: {row} <")
            else:
                print(f"  Row# {r+1}: {row}  ")
        
    def set_row(self, rowno, str):
        col=0
        for c in str:
            if c in ("0123456789"):
                self.board[rowno][col] = int(c)
                col+=1
                if col > 8:
                    return

    def input_board(self):
        for r in range(9):
            self.print_board(r)
            str = input(f"Now enter row# {r+1}: ")
            self.set_row(r, str)

    def rows_are_legal(self):
        for r,row in enumerate(self.board):
            legal_values = { _+1 for _ in range(9) }
            for c,val in enumerate(row):
                if val == 0:
                    pass
                elif val in legal_values:
                    legal_values.remove(val)
                else:
                    print(f"Value {val} found twice in row {r+1}, second time in column {c+1}.")
                    return False
        return True

    def quadrants_are_legal(self):
        for quadrant in range(9):
            legal_values = { _+1 for _ in range(9) }
            for r in range((quadrant // 3) * 3,(quadrant // 3) + 3):
                for c in range((quadrant  % 3)*3,(quadrant  % 3)*3+3):
                    val = self.board[r][c]
                    if val == 0:
                        pass
                    elif val in legal_values:
                        legal_values.remove(val)
                    else:
                        print(f"Value {val} found twice in quadrant. Last time in row {r+1}, column {c+1}.")
                        return False
        return True

    def columns_are_legal(self):
        for c in range(9):
            legal_values = { _+1 for _ in range(9) }
            for r in range(9):
                val = self.board[r][c]
                if val == 0:
                    pass
                elif val in legal_values:
                    legal_values.remove(val)
                else:
                    print(f"Value {val} found twice in column {c+1}, second time in row {r+1}.")
                    return False
        return True

    def board_is_legal(self):
        return self.rows_are_legal() and self.quadrants_are_legal() and self.columns_are_legal()

    def solve(self):
        for r in range(9):
            for c in range(9):
                val = self.board[r][c]
                if val == 0:
                    for v in range(1,10):
                        self.board[r][c] = v
                        if self.board_is_legal() and self.solve():
                            return True
                        else:
                            self.board[r][c] = 0
                    return False
        return True

