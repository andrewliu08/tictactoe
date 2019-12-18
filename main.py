import pygame
from classes import Board, Mark, Button
import minimaxAI
pygame.init()

pygame.display.set_caption("Tic Tac Toe")
winWidth = 500
winHeight = 550
win = pygame.display.set_mode((winWidth, winHeight))
winColour = (255, 255, 255)
win.fill(winColour)

largeSize = 350
gridPos = (75, 175)
grid = Board(gridPos, largeSize)
grid.drawGrid(win)
playX = Button('Play X', 75, 50, Mark.xcolour)
playO = Button('Play O', winWidth-75-Button.width, 50, Mark.ocolour)
pygame.display.update()

depth = 100
gameWin = (False, '')
gameTie = False
run = True
while run:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        run = False

    if not Button.clicked:
        # mouse hovered over button
        mouse = pygame.mouse.get_pos()
        if playX.hover(win, mouse):
            pygame.display.update()
        elif playO.hover(win, mouse):
            pygame.display.update()
        else:
            playX.draw(win, False)
            playO.draw(win, False)
            pygame.display.update()
        # mouse clicks a button setting human player
        if event.type == pygame.MOUSEBUTTONUP:
            if playX.click(win, mouse):
                pygame.display.update()
                grid.setPlayers('X')
            elif playO.click(win, mouse):
                pygame.display.update()
                grid.setPlayers('O')

    elif grid.humanTurn():
        if event.type == pygame.MOUSEBUTTONUP:
            # mouse clicked on grid
            column = grid.findColumn(event.pos[0])
            row = grid.findRow(event.pos[1])
            grid.update(win, row, column)
            gameWin = (grid.checkWin(grid.human), grid.human)
            gameTie = grid.checkTie()
            pygame.display.update()
            grid.nextTurn()

    else:
        aimove = minimaxAI.bestMove(grid.squares, depth, grid.ai)
        grid.update(win, aimove[0], aimove[1])
        pygame.display.update()
        gameWin = (grid.checkWin(grid.ai), grid.ai)
        gameTie = grid.checkTie()
        grid.nextTurn()

    if gameWin[0] or gameTie:
        pygame.time.delay(700)
        win.fill(winColour)
        font = pygame.font.Font('freesansbold.ttf', 64)
        if gameTie:
            text = font.render('Tie Game', True, Mark.ocolour)
        elif gameWin[1] == 'X':
            text = font.render('X Wins', True, Mark.xcolour)
        elif gameWin[1] == 'O':
            text = font.render('O Wins', True, Mark.ocolour)
        textRect = text.get_rect()
        textRect.center = (winWidth // 2, winHeight // 2)
        win.blit(text, textRect)
        pygame.display.update()
        pygame.time.delay(1500)
        run = False

pygame.quit()
