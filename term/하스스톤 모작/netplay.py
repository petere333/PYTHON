from card import *
from random import *
from pico2d import *
from math import *
import mq

class HomeState:
    def __init__(self):
        self.hp=home.hp
        self.hands=len(home.hand)
        self.idx=99
        self.fields=0
    def update(self):
        self.hp=home.hp
        self.hands=len(home.hand)
        if home.field is not None:
            self.fields=1
        if self.fields == 1:
            self.idx=home.field[0].index
    def tostring(self):
        return mq.myid+"%02d"%self.hp+"%02d"%self.hands+"%d"%self.fields+"%02d"%self.idx
class HomePlayer:
    def __init__(self):
        self.hp = 30
        self.hand = []
        self.deck = []
        self.selected = -1
        self.state = 0
        self.field = None
        self.taljin = 1

    def createdeck(self):
        count = 0
        while (count < 30):
            newcard = Card()
            newcard.get(randint(0, 22))
            self.deck.append(newcard)
            count += 1

        update_canvas()

    def drawCard(self):

        if len(self.deck) > 0 and len(self.hand) < 10:
            angle = atan2(150, 740 - 70 * len(self.hand))
            x = 790
            y = 220
            while x > 50 + 70 * len(self.hand) and y > 70:
                clear_canvas()
                pane.draw(480, 270)
                self.printhand()
                self.printfield()
                self.printhp()
                cardback.draw(x, y)
                x -= 40 * cos(angle)
                y -= 40 * sin(angle)
                delay(0.01)
                update_canvas()

            index = randint(0, len(self.deck) - 1)
            newcard2 = self.deck[index]
            self.hand.append(newcard2)
            self.deck.remove(self.deck[index])

            clear_canvas()
            pane.draw(480, 270)
            self.printfield()
            self.printhand()
            self.printhp()
            update_canvas()

        if len(self.deck) <= 0:
            self.hp -= self.taljin
            self.taljin += 1
            clear_canvas()
            pane.draw(480, 270)
            self.printhand()
            self.printfield()
            self.printhp()
            update_canvas()

    def printhighlight(self):
        if self.selected >= 0:
            highlight = load_image("./res/image/select.png")
            highlight.draw(50 + 70 * self.selected, 90)

    def printhand(self):
        i = 0
        while i < len(self.hand):
            self.hand[i].image.draw(50 + 70 * i, 70)
            self.printhighlight()
            i += 1

    def printfield(self):
        index = 0
        if self.field is not None:
            self.field.image.draw(480, 230)
            index += 1

    def end(self):

        if self.selected >= 0:
            if len(self.field) > 0:
                self.field.remove(self.field[0])
            self.field.append(self.hand[self.selected])
            self.hand.remove(self.hand[self.selected])
            state.update()
            mq.client.publish(mq.topic, state)
        else:
            self.hp-=self.taljin
            self.taljin+=1
        self.selected = -1
        state.update()
        mq.client.publish(mq.topic, state)
        repaint()

    def printhp(self):
        font30.draw(465, 120, "%d" % self.hp, (255, 255, 255))



class AI:

    def __init__(self):
        self.hp = 30
        self.hands=0
        self.field=Card()

    def printhand(self):

            self.hands=int(mq.cardget[4:6])
            i = 0
            while (i < self.hands):
                cardback.draw(50 + 70 * i, 470)
                i += 1

            print("printhand")
    def printfield(self):
        if (mq.cardget[7:]!="99"):
            self.field.get(int(mq.cardget[7:]))
            self.field.image.draw(480, 310)

            print("printfield")

    def printhp(self):

            self.hp = int(mq.cardget[2:4])
            font30.draw(465, 420, "%d" % self.hp, (255, 255, 255))

            print("printhp")


pane = load_image('./res/image/board.png')
cardback = load_image("./res/image/back.png")
font30 = load_font("./res/font/text.ttf", 30)

home=HomePlayer()
away=AI()
state=HomeState()
home.createdeck()

def repaint():
    state.update()
    mq.client.publish(mq.topic,state.tostring())
    print("sent")
    delay(5)
    print(mq.cardget)
    clear_canvas()
    pane.draw(480, 270)
    home.printhand()
    home.printfield()
    home.printhp()
    away.printhand()
    away.printhp()
    away.printfield()
    update_canvas()