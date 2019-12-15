import pygame
from classes import Board, Mark
pygame.init()

pygame.display.set_caption("Tic Tac Toe")
win = pygame.display.set_mode((500, 450))
winColour = (255, 255, 255)
win.fill(winColour)

largeSize = 350
grid = Board((75,40), largeSize)
grid.drawGrid(win)
pygame.display.update()

run = True
while run:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        run = False

    if event.type == pygame.MOUSEBUTTONUP:
        grid.update(win, event.pos)
        pygame.display.update()
        gameWin = grid.checkWin()
        gameTie = grid.checkTie()
        if gameWin[0] or gameTie[0]:
            pygame.time.delay(150)
            grid.updateWin(win, gameWin, gameTie)
            pygame.display.update()
            pygame.time.delay(1000)
            run = False

pygame.quit()
