from player import *
from netplay import *
import mq


def close_state():
    clear_canvas()
    close.draw(480,270)
    update_canvas()
    delay(2)
    quit(0)

def result_state(result):
    if(result==2):
        draw.draw(480, 270)
        update_canvas()
        goback = 0
        while goback == 0:
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEBUTTONDOWN:
                    goback = 1
                elif event.type == SDL_QUIT:
                    close_state()

    elif (result == 1):
        victory.draw(480, 270)
        update_canvas()
        goback = 0
        while goback == 0:
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEBUTTONDOWN:
                    goback = 1
                elif event.type == SDL_QUIT:
                    close_state()
    elif (result == -1):
        defeat.draw(480, 270)
        update_canvas()
        goback = 0
        while goback == 0:
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEBUTTONDOWN:
                    goback = 1
                elif event.type == SDL_QUIT:
                    close_state()
    myChar.hp=30
    ai.hp=30
    myChar.hand=[]
    myChar.deck=[]
    ai.hand=[]
    ai.deck=[]
    myChar.createdeck()
    ai.createdeck()
    myChar.taljin=1
    ai.taljin=1
    myChar.field=[]
    ai.field=[]
    myChar.state=0
    ai.state=0

    menu_state()
def wait_net_state():
    mq.connect()
    waitsec=0
    matched=False
    while (waitsec<10):
        mq.sendok()
        waitsec+=1
        if mq.cardget != mq.myid and mq.cardget != None and mq.cardget!="Sending from Unity3D!!!":
            matched=True
            break
        delay(1)
    if(matched==True):
        print("matched")
        net_start_state()
    else:
        print("not matched")
        menu_state()


def net_start_state():
    clear_canvas()
    pane.draw(480, 270)
    home.drawCard()
    home.drawCard()
    home.drawCard()
    home.drawCard()
    update_canvas()

    repaint()
    print("repaint")
    delay(1)
    mq.client.disconnect()

    goback = 0
    while goback == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:

                goback = 1
            elif event.type == SDL_QUIT:
                close_state()
    menu_state()

def single_start_state():
    update_canvas()
    clear_canvas()

    pane.draw(480, 270)
    myChar.drawCard()
    myChar.drawCard()
    myChar.drawCard()
    myChar.drawCard()
    ai.drawCard()
    ai.drawCard()
    ai.drawCard()
    ai.drawCard()
    play_single_state()



def help_state():
    help.draw(480, 270)
    update_canvas()
    goback = 0
    while goback == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:

                goback = 1
            elif event.type==SDL_QUIT:
                close_state()
    menu_state()


def card_list_state():
    list.draw(480, 270)
    update_canvas()
    goback = 0
    while goback == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:

                goback = 1
            elif event.type==SDL_QUIT:
                close_state()
    menu_state()


def invalid_state():
    invalid.draw(480, 270)
    update_canvas()
    goback = 0
    while goback == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:

                goback = 1
            elif event.type==SDL_QUIT:
                close_state()
    menu_state()


def play_single_state():
    finished = 0
    while finished == 0:
        events = get_events()

        for event in events:

            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 539 - event.y
                if myChar.state == 0:
                    index = 0
                    while index < len(myChar.hand):
                        if x >= 15 + 70 * index and x <= 85 + 70 * index and y >= 0 and y <= 130:
                            if myChar.selected == index:
                                myChar.selected = -1
                            else:
                                myChar.selected = index
                            repaint()
                        index += 1
                    if x >= 730 and x <= 800 and y <= 310 and y >= 275:
                        myChar.end()
                        ai.end()

                        fight(myChar, ai)
                        if (myChar.hp > 0 and ai.hp > 0):
                            myChar.drawCard()
                            ai.drawCard()
                            break
                        elif (myChar.hp <= 0 and ai.hp > 0):

                            finished=-1
                            break


                        elif (myChar.hp > 0 and ai.hp <= 0):

                            finished=1
                            break

                        else:

                            finished=2
                            break
            elif event.type==SDL_QUIT:
                close_state()
    result_state(finished)

def menu_state():
    print("menu")
    clear_canvas()

    title.draw(480, 270)
    update_canvas()
    mode = 0
    while mode == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 539 - event.y
                if 400 < x <= 560 and y > 360 and y <= 390:
                    mode = 1
                elif x > 390 and x <= 570 and y > 320 and y <= 350:
                    mode = 2
                elif (x > 390 and x <= 570 and y > 280 and y <= 310):
                    mode = 5
                elif (x > 400 and x <= 560 and y > 240 and y <= 270):
                    mode = 5
                elif (x > 140 and x <= 220 and y > 20 and y <= 100):
                    mode = 5
                elif (x > 220 and x <= 310 and y > 20 and y <= 100):
                    mode = 3
                elif (x > 350 and x <= 440 and y > 50 and y <= 110):
                    mode = 5
                elif (x > 440 and x <= 610 and y > 50 and y <= 110):
                    mode = 4
            elif event.type==SDL_QUIT:
                close_state()
    if mode == 1:
        wait_net_state()
    elif mode == 2:
        loading.draw(480, 270)
        delay(3)
        single_start_state()
    elif mode == 3:
        help_state()
    elif mode == 4:
        card_list_state()
    elif mode == 5:
        invalid_state()

close=load_image('./res/image/close.png')
victory = load_image('./res/image/victory.png')
defeat = load_image('./res/image/defeat.png')
draw = load_image('./res/image/draw.png')
list = load_image('./res/image/list.png')
help = load_image('./res/image/help.png')
loading = load_image('./res/image/loading.png')
invalid = load_image('./res/image/invalid.png')
pane = load_image('./res/image/board.png')
title = load_image('./res/image/title.png')
matching=load_image('./res/image/matching.png')