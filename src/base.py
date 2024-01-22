"""
project_name base module.

This is the principal module of the project_name project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

from __future__ import annotations
from sudoku import Sudoku
import random

class SudokuBoard:    
    # initialise the board, default size is 3x3 and default difficulty is 0.5

    # TODO: change how size is handled. currently changes to size doesn't instantly change board, however for setting etc. it is taking from the size variable instead of board
    def __init__(self, size: int = 3, difficulty: float = 0.5):
        self._size = size
        self._difficulty = difficulty
        self._puzzle = self._generate_board()

    def _generate_board(self, board: list[list[int]] = None) -> Sudoku:
        """Generates a new Sudoku board with the given size and difficulty"""
        return Sudoku(self._size, board).difficulty(self._difficulty)
    
    @property
    def size(self) -> int:
        """Returns the size of the Sudoku board"""
        return self._size
    
    @size.setter
    def size(self, value: int) -> None:
        """Sets the size of the Sudoku board"""
        if 2 <= value <= 4:
            self._size = value
            self._puzzle = self._generate_board()
        else:
            raise ValueError("Size must be between 2 and 4")
        
    @property
    def difficulty(self) -> float:
        """Returns the difficulty of the Sudoku board"""
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, value: float) -> None:
        """Sets the difficulty of the Sudoku board"""
        if 0 < value < 1:
            self._difficulty = value
            self._puzzle = self._generate_board()
        else:
            raise ValueError("Difficulty must be between 0 and 1")
        
    @property
    def puzzle(self) -> Sudoku:
        """Returns the Sudoku board"""
        return self._puzzle
    
    @puzzle.setter
    def puzzle(self, board: list[list[int]]) -> None:
        """Sets the Sudoku board"""
        # TODO: validate the board before setting it (see: https://pypi.org/project/py-sudoku/)
        # TODO: check how setting with a list works
        self._puzzle = self._generate_board(board)
    
    def new_board(self) -> None:
        """Updates the Sudoku board"""
        self._puzzle = self._generate_board()

    def get_board_array(self) -> list[list[int]]:
        """Gets the Sudoku board as a 2D array"""
        return self._puzzle.board
    
    def print_board(self) -> None:
        """Prints the Sudoku board to the terminal"""
        self._puzzle.show()

    def get_board_cell(self, row: int, col: int) -> int:
        """Gets the value of a cell in the Sudoku board"""
        return self._puzzle.board[row][col]
    
    def set_board_cell(self, row: int, col: int, value: int) -> None:
        """Sets the value of a cell in the Sudoku board"""
        # check if value is valid for board size
        if (0 < value <= self._size**2) and isinstance(value, int):
            # check if row and column are valid for board size
            if ( 0 <= row < self._size) and (0 <= col < self._size):
                self._puzzle.board[row][col] = value
            else:
                raise ValueError(f'Row and column must be between 0 and {self._size}')
        else:
            raise ValueError(f'Value must be between 1 and {self._size**2}')

    def get_board_row(self, row: int) -> list[int]:
        """Gets a row of the Sudoku board"""
        return self._puzzle.board[row]
    
    def get_board_col(self, col: int) -> list[int]:
        """Gets a column of the Sudoku board"""
        return [row[col] for row in self._puzzle.board]
    
    def get_board_box(self, row: int, col: int) -> list[int]:
        """Gets a box of the Sudoku board"""
        # TODO: consider how we want to do this. either index the boxes within the board, or return the box of the cell position itself
        box = []
        for i in range(self._size):
            for j in range(self._size):
                box.append(self._puzzle.board[row + i][col + j])
        return box
    
    def get_empty_cells(self) -> list[tuple[int, int]]:
        """Gets the empty cells of the Sudoku board"""
        empty_cells = []
        for i in range(self._size):
            for j in range(self._size):
                if self._puzzle.board[i][j] is None:
                    empty_cells.append((i, j))
        return empty_cells
    
    def get_empty_cell_count(self) -> int:
        """Gets the number of empty cells in the Sudoku board"""
        return len(self.get_empty_cells())
    
    def get_random_empty_cell(self) -> tuple[int, int]:
        """Gets a random empty cell in the Sudoku board"""
        return random.choice(self.get_empty_cells())
