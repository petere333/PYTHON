from pico2d import *
from math import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

cx=400
cy=300
angle=0
frame = 0

while True:
    clear_canvas()
    
    grass.draw(400, 30)
    x=cx+100*cos(angle)
    y=cy+100*sin(angle)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    
    frame = (frame + 1) % 8
    angle+=pi/180

    delay(0.02)

close_canvas()
