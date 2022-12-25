from .sudoku import Sudokuboard
import sys

if __name__ == "__main__":
  print("Hello World in Python")
  print("Add a Sudoku board, line by line:")
  sudokuboard = Sudokuboard()
  # sudokuboard.input_board()
  sudokuboard.set_row(0,"601004")
  sudokuboard.set_row(1,"04000605")
  sudokuboard.set_row(2,"05")
  sudokuboard.set_row(3,"065200003")
  sudokuboard.set_row(4,"0079058")
  sudokuboard.set_row(5,"80000312")
  sudokuboard.set_row(6,"00000003")
  sudokuboard.set_row(7,"08070004")
  sudokuboard.set_row(8,"000800901")

  board_is_ok = sudokuboard.board_is_legal()
  if not board_is_ok:
    print("Sudoku board is not valid.")
  else:
    print("Trying to find a solution to the Sudoku...")
    sudokuboard.solve()
  sudokuboard.print_board()

