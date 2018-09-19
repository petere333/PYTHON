from pico2d import *
from math import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x=0
y=0
xdir=4
ydir=0
frame = 0

while True:
    clear_canvas()
    
    grass.draw(400, 30)
    
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    
    frame = (frame + 1) % 8
    if(x==800 and y==0):
        xdir=0
        ydir=4
    elif(x==800 and y==600):
        xdir=-4
        ydir=0
    elif(x==0 and y==600):
        xdir=0
        ydir=-4
    elif(x==0 and y==0):
        xdir=4
        ydir=0
    x+=xdir
    y+=ydir

    delay(0.02)

close_canvas()
