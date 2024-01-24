from .base import SudokuBoard, SudokuSolver


def main():  # pragma: no cover
    board = SudokuBoard(3, 0.5)
    board.print_board()
    solver = SudokuSolver(board)
    solver.solve()
