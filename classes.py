import pygame
pygame.init()
class Board:
    lineColour = (84, 86, 79)

    def __init__(self, pos, boardSize):
        self.xturn = True
        self.human = ''
        self.ai = ''
        self.pos = pos
        self.boardSize = boardSize
        self.lineWidth = self.boardSize // 45
        self.squares = [[Mark('-') for j in range(3)] for i in range(3)]
        self.squareWidth = self.boardSize // 3
        self.linePos = [[(pos[0]+self.squareWidth, pos[1]),
                         (pos[0]+self.squareWidth, pos[1]+self.boardSize)],
                        [(pos[0]+2*self.squareWidth, pos[1]),
                         (pos[0]+2*self.squareWidth, pos[1]+self.boardSize)],
                        [(pos[0], pos[1]+self.squareWidth),
                         (pos[0]+self.boardSize, pos[1]+self.squareWidth)],
                        [(pos[0], pos[1]+2*self.squareWidth),
                         (pos[0]+self.boardSize, pos[1]+2*self.squareWidth)]]
        self.markPosX = [(self.linePos[0][0][0] - self.squareWidth//2),
                         (self.linePos[1][0][0] - self.squareWidth//2),
                         (self.linePos[1][0][0] + self.squareWidth//2)]
        self.markPosY = [(self.linePos[2][0][1] - self.squareWidth//2),
                         (self.linePos[3][0][1] - self.squareWidth//2),
                         (self.linePos[3][0][1] + self.squareWidth//2)]

    def drawGrid(self, win):
        for line in self.linePos:
            pygame.draw.line(win, Board.lineColour, line[0],
                line[1], self.lineWidth)

    def nextTurn(self):
        self.xturn = not self.xturn

    def setPlayers(self, human):
        self.human = human
        if human == 'X':
            self.ai = 'O'
        else:
            self.ai = 'X'

    def checkWin(self):
        win = False
       # check for horizontal win
        for row in range(3):
            count = 0
            for column in range(3):
                if self.squares[row][column].type !=  player:
                    break
                else:
                    count += 1
            if count == 3:
                win = True
                break

        # check for vertical win
        if not win:
            for column in range(3):
                count = 0
                for row in range(3):
                    if self.squares[row][column].type !=  player:
                        break
                    else:
                        count += 1
                if count == 3:
                    win = True
                    break

        # check for diagonal win
        if not win:
            if self.squares[0][0].type == player and self.squares[1][1].type == player and self.squares[2][2].type == player:
                win = True
            elif self.squares[2][0].type == player and self.squares[1][1].type == player and self.squares[0][2].type == player:
                win = True
            else:
                win = False
        return win

    def checkTie(self):
        for i in range(3):
            for j in range(3):
                if self.squares[i][j].type == '-':
                    return False
        return True

    def update(self, win, pos):
        column = self.findColumn(pos[0])
        row = self.findRow(pos[1])

        # grid spot already taken
        if self.squares[row][column].type != '-':
            self.xturn = not self.xturn # counteract the nextTurn that occurs later
        elif self.xturn:
            self.squares[row][column].type = 'X'
            Mark.drawX(win, self.markPosX[column], self.markPosY[row],
                self.squareWidth//2 - 2*self.lineWidth, self.lineWidth)
        else:
            self.squares[row][column].type = 'O'
            Mark.drawO(win, self.markPosX[column], self.markPosY[row],
                self.squareWidth//2 - 2*self.lineWidth, self.lineWidth)

    def findColumn(self, xpos):
        if xpos < self.linePos[0][0][0]:
            return 0
        elif xpos < self.linePos[1][0][0]:
            return 1
        else:
            return 2

    def findRow(self, ypos):
        if ypos < self.linePos[2][0][1]:
            return 0
        elif ypos < self.linePos[3][0][1]:
            return 1
        else:
            return 2


class Mark:
    xcolour = (84, 86, 79)
    ocolour = (163, 152, 135)

    def __init__(self, type):
        self.type=type

    @staticmethod
    def drawX(win, x, y, shapeWidth, lineWidth):
        pygame.draw.line(win, Mark.xcolour, (x-shapeWidth, y+shapeWidth),
            (x+shapeWidth, y-shapeWidth), lineWidth)
        pygame.draw.line(win, Mark.xcolour, (x+shapeWidth,y+shapeWidth),
            (x-shapeWidth, y-shapeWidth), lineWidth)
    @staticmethod
    def drawO(win, x, y, shapeWidth, lineWidth):
        pygame.draw.circle(win, Mark.ocolour, (x, y),
            shapeWidth, lineWidth)


class Button:
    unclickedColour = (240, 240, 240)
    clickedColour = (200, 200, 210)
    width = 100
    height = 50
    clicked = False
    font = pygame.font.Font('freesansbold.ttf', 16)

    def __init__(self, text, x, y, colour):
        self.text = Button.font.render(text, True, colour)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x + Button.width // 2, y + Button.height // 2)
        self.x = x
        self.y = y

    def draw(self, win, clicked):
        if clicked:
            pygame.draw.rect(win, Button.clickedColour, (self.x, self.y, Button.width, Button.height))
            win.blit(self.text, self.textRect)
        else:
            pygame.draw.rect(win, Button.unclickedColour, (self.x, self.y, Button.width, Button.height))
            win.blit(self.text, self.textRect)

    def hover(self, win, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            self.draw(win, True)
            return True
        else:
            return False

    def click(self, win, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            self.draw(win, True)
            Button.clicked = True
            return True
        else:
            return False
