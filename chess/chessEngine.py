"""
Responsible for storing information about the current game State, also determining valid moves, and keeping move log.

"""
class GameState():
    def __init__(self):
        # Board is an 8x8 2D list
        # Each element of the list contains 2 chars, first tells color and second tells role
        # '--' represents empty space
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.moveLog = []
        self.whiteToMove = True
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"             # Piece has been moved, so starting place is now empty
        self.board[move.endRow][move.endCol] = move.pieceMoved      # Piece has been moved, so ending place is now the piece
        self.moveLog.append(move) # Log so we can undo
        self.whiteToMove = not self.whiteToMove # swap player

class Move():
    ranksToRows = {"1": 7
                   , "2": 6
                   , "3": 5
                   , "4": 4
                   , "5": 3
                   , "6": 2
                   , "7": 1
                   , "8": 0}
    rowsToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0
                   , "b": 1
                   , "c": 2
                   , "d": 3
                   , "e": 4
                   , "f": 5
                   , "g": 6
                   , "h": 7}
    colsToFiles = {v:k for k, v in filesToCols.items()}

    def __init__(self, startSQ, endSQ, board):
        self.startRow = startSQ[0]
        self.startCol = startSQ[1]
        self.endRow = endSQ[0]
        self.endCol = endSQ[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    
    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]
    
    