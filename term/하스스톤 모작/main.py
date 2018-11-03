from pico2d import *
from card import *
from player import *







def playCard():
    finished=0
    while finished==0:
        events=get_events()

        for event in events:

            if event.type==SDL_QUIT:
                font50.draw(450,290,"창을 닫으셨습니다.",(0,0,0))
                font30.draw(400,230,"5초 후 게임이 종료됩니다.",(0,0,0))
                #delay(1)
                finished=1
            elif event.type==SDL_MOUSEBUTTONDOWN:
                x=event.x
                y=539-event.y
                if myChar.state==0:
                    index=0
                    while index<len(myChar.hand):
                        if x>=15+70*index and x<=85+70*index and y>=0 and y<=130:
                                if myChar.selected == index:
                                    myChar.selected = -1
                                else:
                                    myChar.selected=index
                                repaint()
                        index+=1
                    if x>=730 and x<=800 and y<=310 and y>=275:
                        myChar.end()
                        ai.end()

                        fight(myChar,ai)
                        if (myChar.hp>0 and ai.hp>0):
                            myChar.drawCard()
                            ai.drawCard()
                            break
                        elif (myChar.hp <=0 and ai.hp>0):
                            font50.draw(480,270,"패배했습니다!",(0,0,0))
                            font30.draw(480,200,"5초 후 게임이 종료됩니다.",(0,0,0))
                            delay(5)
                            finished=1
                        elif (myChar.hp>0 and ai.hp<=0):
                            font50.draw(480, 270, "승리했습니다!", (0, 0, 0))
                            font30.draw(480, 200, "5초 후 게임이 종료됩니다.", (0, 0, 0))
                            delay(5)
                            finished = 1
                        else:
                            font50.draw(480, 270, "무승부입니다!", (0, 0, 0))
                            font30.draw(480, 200, "5초 후 게임이 종료됩니다.", (0, 0, 0))
                            delay(5)
                            finished = 1






def game_start():


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
    update_canvas()
    playCard()

pane = load_image('./res/image/board.png')
game_start()
