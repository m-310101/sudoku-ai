"""
project_name base module.

This is the principal module of the project_name project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

from sudoku import Sudoku
import random

class SudokuBoard:
    # initialise the board, default size is 3x3 and default difficulty is 0.5
    def __init__(self, size=3, difficulty=0.5):
        self.size = size
        self.difficulty = difficulty
        self.puzzle = self.generateBoard()

    def generateBoard(self):
        return Sudoku(self.size).difficulty(self.difficulty)
    
    def updateBoard(self):
        self.puzzle = self.generateBoard()

    def getBoard(self):
        return self.puzzle

    def getBoardArray(self):
        return self.puzzle.board
    
    def getBoardSize(self):
        return self.size
    
    def getBoardDifficulty(self):
        return self.difficulty
    
    def setBoardSize(self, size):
        self.size = size

    def setBoardDifficulty(self, difficulty):
        self.difficulty = difficulty

    def printBoard(self):
        self.puzzle.show()

    def getBoardCell(self, row, col):
        return self.puzzle.board[row][col]
    
    def setBoardCell(self, row, col, value):
        self.puzzle.board[row][col] = value

    def getBoardRow(self, row):
        return self.puzzle.board[row]
    
    def getBoardCol(self, col):
        return [row[col] for row in self.puzzle.board]
    
    def getBoardBox(self, row, col):
        box = []
        for i in range(self.size):
            for j in range(self.size):
                box.append(self.puzzle.board[row + i][col + j])
        return box
    
    def getBoardEmptyCells(self):
        emptyCells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle.board[i][j] is None:
                    emptyCells.append((i, j))
        return emptyCells
    
    def getBoardEmptyCellsCount(self):
        return len(self.getBoardEmptyCells())
    
    def getBoardEmptyCellsRandom(self):
        return random.choice(self.getBoardEmptyCells())
    

