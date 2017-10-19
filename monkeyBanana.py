#Morgan Baughman
#10/19/17
#monkeyBanana.py 
from random import randint
from ggame import *

#constants
ROWS = 40
COLS = 50
CELL_SIZE = 20

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
    
def moveLeft(event):
     if monkey.x > 0:
        monkey.x -= CELL_SIZE
    
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
    
def moveDown(event):
    monkey.y += CELL_SIZE

def moveBanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE




if __name__ == '__main__':
    
    green = Color(0x006600, 1)
    brown = Color(0x8B4513, 1)
    yellow= Color(0xFFFF00, 1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE, ROWS*CELL_SIZE, LineStyle(1, green), green)
    monkeyBox = RectangleAsset(CELL_SIZE, CELL_SIZE,LineStyle(1, brown), brown)
    bananaBox = RectangleAsset(CELL_SIZE, CELL_SIZE,LineStyle(1, yellow), yellow)
        
    Sprite(jungleBox)
    banana = Sprite(bananaBox,(COLS*CELL_SIZE/2, ROWS*CELL_SIZE/2))
    monkey = Sprite(monkeyBox)
    
    App().listenKeyEvent('keydown' ,'right arrow' ,moveRight)
    App().listenKeyEvent('keydown' ,'left arrow' ,moveLeft)
    App().listenKeyEvent('keydown' ,'up arrow' ,moveUp)
    App().listenKeyEvent('keydown' ,'down arrow' ,moveDown)
    App().run()