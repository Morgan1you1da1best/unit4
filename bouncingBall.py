#Morgan Baughman
#10/27/17
#bouncingBall.py

from random import randint
from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 50

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
    
def moveLeft(event):
     if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
def moveDown(event):
    monkey.y += CELL_SIZE
    if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def updateScore():
    data['score'] += 100
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))



if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    
    
    
    
    green = Color(0x006600, 1)
    brown = Color(0x8B4513, 1)
    yellow= Color(0xFFFF00, 1)
    blue= Color(0x00FFFF, 1)
    
    playBox = RectangleAsset(COLS*CELL_SIZE, ROWS*CELL_SIZE, LineStyle(1, green), green)
    monkeyBox = RectangleAsset(CELL_SIZE, CELL_SIZE,LineStyle(1, blue), blue)
    scoreBox = TextAsset('Score = 0')
        
        
        
    Sprite(playBox)
    monkey = Sprite(monkeyBox)
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    
    App().listenKeyEvent('keydown' ,'right arrow' ,moveRight)
    App().listenKeyEvent('keydown' ,'left arrow' ,moveLeft)
    App().listenKeyEvent('keydown' ,'up arrow' ,moveUp)
    App().listenKeyEvent('keydown' ,'down arrow' ,moveDown)
    App().run()
