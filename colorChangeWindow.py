#Morgan Baughman
#10/18/17
#colorChangeWindow.py


from random import randint
from ggame import *

def mouseClick(event):
    num = randint(1,4)
    
    if num == 1:
        red = Color(0xFF0000, 1)
        redRectangle = RectangleAsset(700, 700, LineStyle(1, red), red)
        Sprite(redRectangle)
        
    elif num == 2:
        lightgreen = Color(0x33FF8D, 1)
        lightgreenRectangle = RectangleAsset(700, 700, LineStyle(1, lightgreen), lightgreen)
        Sprite(lightgreenRectangle)
        
    elif num == 3:
        green = Color(0x00FF00, 1)
        greenRectangle = RectangleAsset(700, 700, LineStyle(1, green), green)
        Sprite(greenRectangle)
        
    elif num == 4:
        purple = Color(0xE033FF, 1)
        purpleRectangle = RectangleAsset(700, 700, LineStyle(1, purple), purple)
        Sprite(purpleRectangle)

    else:
        blue = Color(0x0000FF, 1)
        blueRectangle = RectangleAsset(700, 700, LineStyle(1, blue), blue)
        Sprite(blueRectangle)

        
App().listenMouseEvent("click", mouseClick)
App().run()
