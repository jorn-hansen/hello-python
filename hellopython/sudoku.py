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