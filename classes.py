import pygame
class Board:
    lineColour = (84, 86, 79)

    def __init__(self, pos, boardSize):
        self.xturn = True
        self.pos = pos
        self.boardSize = boardSize
        self.lineWidth = self.boardSize // 45
        self.squares = [[Mark('empty') for j in range(3)] for i in range(3)]
        self.squareWidth = self.boardSize // 3
        self.linePos = [[(pos[0]+self.squareWidth, pos[1]),
                         (pos[0]+self.squareWidth, pos[1]+self.boardSize)],
                        [(pos[0]+2*self.squareWidth, pos[1]),
                         (pos[0]+2*self.squareWidth, pos[1]+self.boardSize)],
                        [(pos[0], pos[1]+self.squareWidth),
                         (pos[0]+self.boardSize, pos[1]+self.squareWidth)],
                        [(pos[0], pos[1]+2*self.squareWidth),
                         (pos[0]+self.boardSize, pos[1]+2*self.squareWidth)]]

    def drawGrid(self, win):
        for line in self.linePos:
            pygame.draw.line(win, Board.lineColour, line[0],
                line[1], self.lineWidth)

    def checkWin(self):
        win = [False, -1, -1, -1] #(win?, condition, x, y)
        # check for horizontal win
        for row in range(3):
            count = 1
            mark = self.squares[0][row].type
            for column in range(1,3):
                if self.squares[column][row].type !=  mark or mark == 'empty':
                    break
                else:
                    count += 1
            if count == 3:
                win = [True, 0, 0, row]
                break

        # check for vertical win
        if not win[0]:
            for column in range(3):
                count = 1
                mark = self.squares[column][0].type
                for row in range(1,3):
                    if self.squares[column][row].type !=  mark or mark == 'empty':
                        break
                    else:
                        count += 1
                if count == 3:
                    win = [True, 1, column, 0]
                    break

        # check for diagonal win
        if not win[0]:
            mark = self.squares[1][1].type
            if mark != 'empty' and self.squares[0][0].type == mark and self.squares[2][2].type == mark:
                win = [True, 2, 0, 0]
            elif mark != 'empty' and self.squares[2][0].type == mark and self.squares[0][2].type == mark:
                win = [True, 3, 0, 2]
            else:
                win = [False, -1, -1, -1]
        return win

    def checkTie(self):
        for i in range(3):
            for j in range(3):
                if self.squares[i][j].type == 'empty':
                    return [False, -1, -1, -1]
        return [True, 4, -1, -1]

    def updateWin(self, surface, conditions, tie):
        # row win
        if conditions[1] == 0:
            pygame.draw.line(surface, self.lineColour, (conditions[2],conditions[3]),
                (conditions[2],conditions[3]+2*self.squareWidth), self.lineWidth)
        # column win
        elif conditions[1] == 1:
            pygame.draw.line(surface, self.lineColour, (conditions[2],conditions[3]),
                (conditions[2]+2*self.squareWidth,conditions[3]), self.lineWidth)
        # diagonal win top left bottom right
        elif conditions[1] == 2:
            pygame.draw.line(surface, self.lineColour, (conditions[2],conditions[3]),
                (conditions[2]-2*self.squareWidth,conditions[3]+2*self.squareWidth), self.lineWidth)
        # diagonal win top right bottom left
        elif condition[1] == 3:
            pygame.draw.line(surface, self.lineColour, (conditions[2],conditions[3]),
                (conditions[2]+2*self.squareWidth,conditions[3]-2*self.squareWidth), self.lineWidth)
        # tie
        else:
            pygame.draw.line(surface, self.lineColour, (conditions[2],conditions[3]),
                (conditions[2]+2*self.squareWidth,conditions[3]-2*self.squareWidth), self.lineWidth)

    def update(self, win, pos):
        xpos = self.findSquareX(pos[0])
        ypos = self.findSquareY(pos[1])
        if self.squares[xpos[1]][ypos[1]].type != 'empty':
            self.xturn = self.xturn
        elif self.xturn:
            self.squares[xpos[1]][ypos[1]].type = 'X'
            Mark.drawX(win, xpos[0], ypos[0],
                self.squareWidth//2 - 2*self.lineWidth, self.lineWidth)
            self.xturn = not self.xturn
        else:
            self.squares[xpos[1]][ypos[1]].type = 'O'
            Mark.drawO(win, xpos[0], ypos[0],
                self.squareWidth//2 - 2*self.lineWidth, self.lineWidth)
            self.xturn = not self.xturn

    def findSquareX(self, xpos):
        if xpos < self.linePos[0][0][0]:
            return (self.linePos[0][0][0] - self.squareWidth//2, 0)
        elif xpos < self.linePos[1][0][0]:
            return (self.linePos[1][0][0] - self.squareWidth//2, 1)
        else:
            return (self.linePos[1][0][0] + self.squareWidth//2, 2)

    def findSquareY(self, ypos):
        if ypos < self.linePos[2][0][1]:
            return (self.linePos[2][0][1] - self.squareWidth//2, 0)
        elif ypos < self.linePos[3][0][1]:
            return (self.linePos[3][0][1] - self.squareWidth//2, 1)
        else:
            return (self.linePos[3][0][1] + self.squareWidth//2, 2)


class Mark:
    xcolour = (84, 86, 79)
    ocolour = (163, 152, 135)

    def __init__(self, type):
        self.type=type

    @staticmethod
    def drawX(win, x, y, shapeWidth, lineWidth):
        pygame.draw.line(win, Mark.xcolour, (x-shapeWidth,y+shapeWidth),
            (x+shapeWidth, y-shapeWidth), lineWidth)
        pygame.draw.line(win, Mark.xcolour, (x+shapeWidth,y+shapeWidth),
            (x-shapeWidth, y-shapeWidth), lineWidth)
    @staticmethod
    def drawO(win, x, y, shapeWidth, lineWidth):
        pygame.draw.circle(win, Mark.ocolour, (x, y),
            shapeWidth, lineWidth)
