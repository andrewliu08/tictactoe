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
gridPos = (75, 175)
grid = Board(gridPos, largeSize)
grid.drawGrid(win)
playX = Button('Play X', 75, 50, Mark.xcolour)
playO = Button('Play O', winWidth-75-Button.width, 50, Mark.ocolour)
pygame.display.update()

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

    else:
        if event.type == pygame.MOUSEBUTTONUP:
            # mouse clicked on grid
            grid.update(win, event.pos)
            pygame.display.update()
            if grid.checkWin() or grid.checkTie():
                pygame.time.delay(750)
                win.fill(winColour)
                font = pygame.font.Font('freesansbold.ttf', 64)
                if grid.xturn:
                    text = font.render('X Wins', True, Mark.xcolour)
                else:
                    text = font.render('O Wins', True, Mark.ocolour)
                textRect = text.get_rect()
                textRect.center = (winWidth // 2, winHeight // 2)
                win.blit(text, textRect)
                pygame.display.update()
                pygame.time.delay(1500)
                run = False

            grid.nextTurn()

pygame.quit()
