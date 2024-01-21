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
    clarence = SudokuBoard(3, 0.7)

    print('\ngetBoard()')
    print(clarence.getBoard())
    print('\ngetBoardArray()')
    print(clarence.getBoardArray())
    print('\ngetBoardSize()')
    print(clarence.getBoardSize())
    print('\ngetBoardDifficulty()')
    print(clarence.getBoardDifficulty())
    print('\nsetBoardSize(4)')
    print(clarence.setBoardSize(4))
    print('\nsetBoardDifficulty(0.4)')
    print(clarence.setBoardDifficulty(0.4))
    print('\nupdateBoard()')
    print(clarence.updateBoard())
    print('\ngetBoard()')
    print(clarence.getBoard())
    print('\nsetBoardCell(3, 5, 12)')
    print(clarence.setBoardCell(3, 5, 12))
    print('\ngetBoardCell(3, 5)')
    print(clarence.getBoardCell(3, 5))
    print('\ngetBoard()')
    print(clarence.getBoard())
    print('\ngetBoardRow(4)')
    print(clarence.getBoardRow(4))
    print('\ngetBoardCol(2)')
    print(clarence.getBoardCol(2))
    print('\ngetBoardBox(4, 0)')
    print(clarence.getBoardBox(4, 0))
    print('\ngetBoardEmptyCells()')
    print(clarence.getBoardEmptyCells())
    print('\ngetBoardEmptyCellsCount()')
    print(clarence.getBoardEmptyCellsCount())
    print('\ngetBoardEmptyCellsRandom()')
    print(clarence.getBoardEmptyCellsRandom())