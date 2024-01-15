
"""
MAIN: Handling user's inputs and displaying current game State
"""

import pygame as p
import chessEngine

WIDTH = HEIGHT  = 512                   # Board's size
DIMENSION       = 8                     # Board's dimension
SQ_SIZE         = HEIGHT / DIMENSION    # Square's size
MAX_FPS         = 15
IMAGES          = {}


"""
To be called ONCE by main()
w - white ; b - black
p - pawn ; R - Rook ; N - Knight ; B - Bishop ; K - King ; Q - Queen
"""
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

"""
Updating graphics as the game goes on based on GameSate
"""
def drawGameState(screen, gameState):
    drawBoard(screen)                   # Draw squares on board
    drawPieces(screen, gameState)       # Draw pieces on top of the squares

"""
Drawing the squares on the board
(Top left square is always light)
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[(row+col) % 2]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)) # left, top, width, height

"""
Drawing the pieces on the board based on the GameState
"""
def drawPieces(screen, gameState):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = gameState.board[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""MAIN"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("white"))
    gameState = chessEngine.GameState()
    clock = p.time.Clock()
    loadImages()
    gameRun = True
    while gameRun:
        for e in p.event.get():
            if e.type == p.QUIT:
                gameRun = False
        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()