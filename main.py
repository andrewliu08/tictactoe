import pygame
from classes import Board, Mark, Button
pygame.init()

pygame.display.set_caption("Tic Tac Toe")
winWidth = 500
winHeight = 550
win = pygame.display.set_mode((winWidth, winHeight))
winColour = (255, 255, 255)
win.fill(winColour)

largeSize = 350
grid = Board((75,175), largeSize)
grid.drawGrid(win)
playX = Button('Play X', 75, 50, Mark.xcolour)
playO = Button('Play O', winWidth-75-Button.width, 50, Mark.ocolour)
playX.draw(win)
playO.draw(win)
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
            pygame.time.delay(500)

            win.fill(winColour)
            font = pygame.font.Font('freesansbold.ttf', 64)
            text = font.render('X Wins', True, Mark.xcolour)
            textRect = text.get_rect()
            textRect.center = (winWidth // 2, winHeight // 2)
            win.blit(text, textRect)
            pygame.display.update()
            pygame.time.delay(1000)
            run = False

pygame.quit()
