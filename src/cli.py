"""CLI interface for project_name project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

from .base import SudokuBoard

def main():  # pragma: no cover
    print("This will do something")
    board = SudokuBoard(3, 0.7)
    board.print_board()

    # print('\ngetBoard()')
    # print(board.getBoard())
    # print('\ngetBoardArray()')
    # print(board.getBoardArray())
    # print('\nboard size')
    # print(board.size)
    # print('\nboard difficulty')
    # print(board.difficulty)
    # print('\nset board size to 4')
    # board.size = 4
    # print(board.size)
    # print('\nset board difficulty to 0.4')
    # board.difficulty = 0.4
    # print(board.difficulty)
    # print('\nupdateBoard()')
    # print(board.updateBoard())
    # print('\ngetBoard()')
    # print(board.getBoard())
    # print('\nsetBoardCell(3, 5, 12)')
    # print(board.setBoardCell(3, 5, 12))
    # print('\ngetBoardCell(3, 5)')
    # print(board.getBoardCell(3, 5))
    # print('\ngetBoard()')
    # print(board.getBoard())
    # print('\ngetBoardRow(4)')
    # print(board.getBoardRow(4))
    # print('\ngetBoardCol(2)')
    # print(board.getBoardCol(2))
    # print('\ngetBoardBox(4, 0)')
    # print(board.getBoardBox(4, 0))
    # print('\ngetBoardEmptyCells()')
    # print(board.getBoardEmptyCells())
    # print('\ngetBoardEmptyCellsCount()')
    # print(board.getBoardEmptyCellsCount())
    # print('\ngetBoardEmptyCellsRandom()')
    # print(board.getBoardEmptyCellsRandom())