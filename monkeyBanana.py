#Morgan Baughman
#10/19/17
#monkeyBanana.py 

from ggame import *

#constants
ROWS = 40
COLS = 50
CELL_SIZE = 20


if __name__ == '__main__':
    
    green = Color(0x006600, 1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE, ROWS*CELL_SIZE, LineStyle(1, green), green)
    
    Sprite(jungleBox)
    
    App().run()