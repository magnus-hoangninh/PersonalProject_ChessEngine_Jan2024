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
    
    """
    Takes a move as parameter and executes it (will not work for castling / en passant / pawn promotion)
    """
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"             # Piece has been moved, so starting place is now empty
        self.board[move.endRow][move.endCol] = move.pieceMoved      # Piece has been moved, so ending place is now the piece
        self.moveLog.append(move) # Log so we can undo
        self.whiteToMove = not self.whiteToMove # swap player

    """
    Undo the last move
    """
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    """
    All moves considering checks
    """
    def generateValidMoves(self):
        return self.generatePossibleMoves()

    """
    All moves without considering checks
    """
    def generatePossibleMoves(self):
        moves = [Move((0, 0), (2, 0), self.board)]
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == "w" and self.whiteToMove) and (turn == "b" and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.getPawnMoves(row, col, moves)
                    elif piece == 'R':
                        self.getRookMoves(row, col, moves)
        return moves
    
    """
    Get all the possible moves of a pawn given its location and add the moves to moves list
    """
    def getPawnMoves(self, row, col, moves):
        pass

    """
    Get all the possible moves of a rook given its location and add the moves to moves list
    """
    def getRookMoves(self, row, col, moves):
        pass

    """
    Get all the possible moves of a bishop given its location and add the moves to moves list
    """
    def getBishopMoves(self, row, col, moves):
        pass

    """
    Get all the possible moves of a knight given its location and add the moves to moves list
    """
    def getKnightMoves(self, row, col, moves):
        pass

    """
    Get all the possible moves of a queen given its location and add the moves to moves list
    """
    def getQueenMoves(self, row, col, moves):
        pass

    """
    Get all the possible moves of a King given its location and add the moves to moves list
    """
    def getKingMoves(self, row, col, moves):
        pass
    
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
    
    