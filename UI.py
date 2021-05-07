import pygame
import random

COLORS = [
    (255, 255, 255), #WHITE
    (0,0,0), #BLACK
    (255, 255, 240), #CREAM
    (255, 0, 0), #RED
    (136, 140, 141), #STONE
]

STATES = [
    'NEW GAME',
    'NEW PIECE',
    'PLAY'
]

INPUT = [
    'UP', 
    'DOWN', 
    'RIGHT', 
    'LEFT', 
    'SPACE',
    'NONE'
]

class Piece:
    def __init__(self, pos):
        super().__init__()
        self.type = random.randint(0,3)
        self.poss = [pos]

        if self.type == 1:
            self.poss.append((pos[0]+1, pos[1]))
            self.poss.append((pos[0]+1, pos[1]+1))
            self.poss.append((pos[0]+1, pos[1]+2))

        if self.type == 2:
            self.poss.append((pos[0], pos[1]+1))
            self.poss.append((pos[0], pos[1]+2))
            self.poss.append((pos[0], pos[1]+3))

        if self.type == 3:
            self.poss.append((pos[0]+1, pos[1]+1))
            self.poss.append((pos[0], pos[1]+1))
            self.poss.append((pos[0]+1, pos[1]))

        if self.type == 4:
            self.poss.append((pos[0], pos[1]+1))
            self.poss.append((pos[0], pos[1]+2))
            self.poss.append((pos[0]+1, pos[1]+1))

class Tetris:
    def stageDet(self):
        newGame = True
        newPiece = False
        for i in self.grid:
            for j in i:
                if j.color != 2:
                    newPiece = True
                    if j.color == 3:
                        return 2
        if newPiece:
            return 1
        elif newGame:                
            return 0
   
    def newBlock(self):
        self.piece = Piece((1,2))
        for i in self.piece.poss:
            self.grid[i[0]][i[1]].color = 3
    
    def play(self, input):
        self.state = self.stageDet()
        if self.state == 0:
            self.newBlock()
        else:
            print(input)

        return self.grid

    def __init__(self, grid):
        self.grid = grid
        self.state = self.stageDet()

class Block:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

class Buttons(pygame.sprite.Sprite):
    def __init__(self, path, pos, changes):
        super().__init__()
        self.image =  pygame.transform.scale(pygame.image.load(path), (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.changes = changes

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.to = self.changes
                    print(self.to)


class UI:
    def rect(self, color, pos):
        pygame.draw.rect(self.screen, color, pos)
    
    def drawGrid(self):

        for i in range(self.N[0]):
            for j in range(self.N[1]):
                color = self.grid[i][j].color
                x = self.grid[i][j].x
                y = self.grid[i][j].y
                width = self.grid[i][j].width
                self.rect(COLORS[color], [x, y, width, width])


    def play(self, inputList):
        if len(inputList) > 0:
            self.grid = self.tetris.play(INPUT.index(inputList[0]))
        else:
            self.grid = self.tetris.play(5)
        self.drawGrid()

    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.to = (False, True, False)
        self.rect(COLORS[2], [500, 0, 300, 600])
        
        #MAKING THE GRID
        self.N = (20, 10)
        grid = []
        xM = 100
        yM = 25
        for x in range(self.N[0]):
            row = []
            for y in range(self.N[1]):
                block = Block(xM, yM, 25, 2)
                row.append(block)
                self.rect(COLORS[block.color], [block.x, block.y, block.width, block.width])
                xM += 26
            yM += 26
            xM = 100
            grid.append(row)
        self.grid = grid

        #BUTTONS
        self.playB = Buttons('images/play-arrow.png', (650, 100), (True, False, False))
        self.pauseB = Buttons('images/pause.png', (650, 300), (False, True, False))
        self.aiB = Buttons('images/chip.png', (650, 500), (False, False, True))
        self.buttonsGroup = pygame.sprite.Group()
        self.buttonsGroup.add(self.playB)
        self.buttonsGroup.add(self.pauseB)
        self.buttonsGroup.add(self.aiB)

        #TETRIS
        self.tetris = Tetris(self.grid)

