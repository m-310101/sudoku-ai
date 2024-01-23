"""
Algos for solving sudoku:
line checks, see if number is only instance in the line
box checks, see if number is only instance in the box
solo number, see if cell only has one possible number

pen notes:
check if 2 numbers are the only possible numbers in a box/line, if so, remove them from pen notes of other cells in the box/line
same with 3 numbers, 4 numbers etc.
if only locations for number in box fall on same line, remove from pen notes of other cells in line/box
"""


from __future__ import annotations
from sudoku import Sudoku
import random

class SudokuBoard:    
    # initialise the board, default size is 3x3 and default difficulty is 0.5

    # TODO: change how size is handled. currently changes to size doesn't instantly change board, however for setting etc. it is taking from the size variable instead of board
    def __init__(self, size: int = 3, difficulty: float = 0.5):
        self._size = size
        self._width = self._height = size**2
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
            self._width = self._height = value ** 2
            self._puzzle = self._generate_board()
        else:
            raise ValueError("Size must be between 2 and 4")
        
    @property
    def height(self) -> int:
        """Returns the height of the Sudoku board"""
        return self._height
        
    @property
    def width(self) -> int:
        """Returns the width of the Sudoku board"""
        return self._width

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
        if (0 < value <= (self._size ** 2)) and isinstance(value, int):
            # check if row and column are valid for board size
            if ( 0 <= row < (self._height)) and (0 <= col < (self._width)):
                self._puzzle.board[row][col] = value
            else:
                raise ValueError(f'Row and column must be between 0 and {(self._size ** 2)}')
        else:
            raise ValueError(f'Value must be between 1 and {(self._size ** 2)}')

    def get_board_row(self, row: int) -> list[int]:
        """Gets a row of the Sudoku board"""
        return self._puzzle.board[row]
    
    def get_board_col(self, col: int) -> list[int]:
        """Gets a column of the Sudoku board"""
        return [row[col] for row in self._puzzle.board]
    
    def get_board_box(self, row: int, col: int) -> list[int]:
        """Gets a box of the Sudoku board"""
        # TODO: consider how we want to do this. either index the boxes within the board, or return the box of the cell position itself
        box_pos = (row // self._size, col // self._size)
        box = []
        for i in range(self._size):
            for j in range(self._size):
                box.append(self._puzzle.board[i + (self._size * box_pos[0])][j + (self._size * box_pos[1])])
        return box
    
    def get_empty_cells(self) -> list[tuple[int, int]]:
        """Gets the empty cells of the Sudoku board"""
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if self._puzzle.board[i][j] is None:
                    empty_cells.append((i, j))
        return empty_cells
    
    def get_empty_cell_count(self) -> int:
        """Gets the number of empty cells in the Sudoku board"""
        return len(self.get_empty_cells())
    
    def get_random_empty_cell(self) -> tuple[int, int]:
        """Gets a random empty cell in the Sudoku board"""
        return random.choice(self.get_empty_cells())

class SudokuSolver:
    def __init__(self, board: SudokuBoard):
        self._board = board
        self._empty_cells = self._board.get_empty_cells()
        self._pen_notes = self._generate_pen_notes()

    def _generate_pen_notes(self) -> list[list[list[int]]]:
        possiblity_grid = [[[] for _ in range(self._board.width)] for _ in range(self._board.height)]

        for (row, col) in self._empty_cells:
            for value in range((self._board.size ** 2)):
                if self._validate_cell(row, col, value + 1):
                    possiblity_grid[row][col].append(value + 1)

        return possiblity_grid

    def _validate_cell(self, row: int, col: int, value: int) -> bool:
        """Validates a cell in the Sudoku board"""
        if (value not in self._board.get_board_row(row)):
            if (value not in self._board.get_board_col(col)):
                if (value not in self._board.get_board_box(row, col)):
                    return True
                
        return False
    
    def _set_cell(self, row: int, col: int, value: int) -> None:
        """Sets a cell in the Sudoku board"""
        self._board.set_board_cell(row, col, value)
        self._empty_cells = self._board.get_empty_cells()
        self._pen_notes = self._generate_pen_notes()
    
    def _lonely_cell(self, row: int, col: int) -> bool:
        """Checks if a cell is the only possible cell in a row, column or box"""
        return (len(self._pen_notes[row][col]) == 1)
    
    def _lonely_row(self, row: int, col: int, value: int) -> bool:
        """Checks if a cell is the only possible cell in a row"""
        row_possibilities = self._pen_notes[row]
        del row_possibilities[col]
        for possibility in row_possibilities:
            if (value in possibility):
                return False
        return True
    
    def _lonely_column(self, row: int, col: int, value: int) -> bool:
        """Checks if a cell is the only possible cell in a column"""
        column_possibilities = [row[col] for row in self._pen_notes]
        del column_possibilities[row]
        for possibility in column_possibilities:
            if (value in possibility):
                return False
        return True
    
    def _lonely_box(self, row: int, col: int, value: int) -> bool:
        """Checks if a cell is the only possible cell in a box"""
        box_pos = (row // self._board.size, col // self._board.size)
        box_possibilities = []
        for i in range(self._board.size):
            for j in range(self._board.size):
                box_possibilities.append(self._pen_notes[i + (self._board.size * box_pos[0])][j + (self._board.size * box_pos[1])])
        relative_index = ((row % self._board.size) * self._board.size) + (col % self._board.size)
        del box_possibilities[relative_index]
        for possibility in box_possibilities:
            if (value in possibility):
                return False
        return True

    def solve(self) -> None:
        """Solves the Sudoku board"""
        index = 0

        while index < len(self._empty_cells):
            row, col = self._empty_cells[index]
            if self._lonely_cell(row, col):
                self._set_cell(row, col, self._pen_notes[row][col][0])
                index = 0
            else:
                for possibility in self._pen_notes[row][col]:
                    if self._lonely_row(row, col, possibility):
                        self._set_cell(row, col, possibility)
                        index = 0
                    elif self._lonely_column(row, col, possibility):
                        self._set_cell(row, col, possibility)
                        index = 0
                    elif self._lonely_box(row, col, possibility):
                        self._set_cell(row, col, possibility)
                        index = 0
