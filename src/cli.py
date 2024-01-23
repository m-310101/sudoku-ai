"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

from .base import SudokuBoard, SudokuSolver

def main():  # pragma: no cover
    print("This will do something")
    board = SudokuBoard(3, 0.5)
    board.print_board()
    solver = SudokuSolver(board)
    solver.solve()
    