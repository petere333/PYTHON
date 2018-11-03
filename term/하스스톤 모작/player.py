from card import *
from random import *
from pico2d import *
from math import *


class Player:
    def __init__(self):
        self.hp = 30
        self.hand = []
        self.deck = []
        self.selected = -1
        self.state = 0
        self.field = []
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
                ai.printhp()
                ai.printhand()
                ai.printfield()
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
            ai.printhp()
            ai.printhand()
            ai.printfield()
            update_canvas()
        if len(self.deck) <= 0:
            self.hp -= self.taljin
            self.taljin += 1
            repaint()
            if self.hp<=0 and ai.hp>0:
                font50.draw(480, 270, "패배했습니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)
            elif self.hp<=0 and myChar.hp<=0:
                font50.draw(480, 270, "무승부입니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)

    def printhighlight(self):
        if self.selected >= 0:
            highlight = load_image("./res/image/select.png")
            highlight.draw(50 + 70 * self.selected, 90)

    def printhand(self):
        i = 0
        while (i < len(self.hand)):
            self.hand[i].image.draw(50 + 70 * i, 70)
            self.printhighlight()
            i += 1

    def printfield(self):
        index = 0
        while index < len(self.field):
            self.field[index].image.draw(480, 230)
            index += 1

    def end(self):

        if self.selected >= 0:
            angle = atan2(160, 430 - 70 * self.selected)
            x = 50 + 70 * self.selected
            y = 70
            while abs(x - 480) > 40 and y < 230:
                clear_canvas()
                pane.draw(480, 270)
                self.printfield()
                self.printhand()
                self.printhp()
                ai.printhp()
                ai.printfield()
                ai.printhand()
                self.hand[self.selected].image.draw(x, y)
                x += 40 * cos(angle)
                y += 40 * sin(angle)
                delay(0.01)
                update_canvas()
            if len(self.field) > 0:
                self.field.remove(self.field[0])
            self.field.append(self.hand[self.selected])
            self.hand.remove(self.hand[self.selected])
        else:
            self.hp-=self.taljin
            self.taljin+=1
            repaint()
            if self.hp<=0 and ai.hp>0:
                font50.draw(480, 270, "패배했습니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)
            elif self.hp<=0 and ai.hp<=0:
                font50.draw(480, 270, "무승부입니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)
        self.selected = -1
        repaint()

    def printhp(self):
        font30.draw(465, 120, "%d" % self.hp, (255, 255, 255))


class AI:
    def __init__(self):
        self.hp = 30
        self.hand = []
        self.deck = []
        self.state = 0
        self.field = []
        self.taljin = 1

    def createdeck(self):
        count = 0
        while (count < 30):
            newcard = Card()
            newcard.get(randint(0, 22))
            self.deck.append(newcard)
            count += 1

    def drawCard(self):

        if len(self.deck) > 0 and len(self.hand) < 10:

            angle = atan2(110, 740 - 70 * len(self.hand))
            x = 790
            y = 360
            while x > 50 + 70 * len(self.hand) and y < 470:
                clear_canvas()
                pane.draw(480, 270)
                self.printhand()
                self.printfield()
                self.printhp()
                myChar.printhp()
                myChar.printhand()
                myChar.printfield()

                cardback.draw(x, y)
                x -= 40 * cos(angle)
                y += 40 * sin(angle)
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
            myChar.printhp()
            myChar.printhand()
            myChar.printfield()
            update_canvas()
        if len(self.deck) <= 0:
            self.hp -= self.taljin
            self.taljin += 1
            repaint()
            if self.hp<=0 and myChar.hp>0:
                font50.draw(480, 270, "승리했습니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)
            elif self.hp<=0 and myChar.hp<=0:
                font50.draw(480, 270, "무승부입니다!", (0, 0, 0))
                font30.draw(480, 200, "3초 후 게임이 종료됩니다.", (0, 0, 0))
                delay(3)
                exit(0)


    def printhand(self):
        i = 0

        while (i < len(self.hand)):
            cardback.draw(50 + 70 * i, 470)
            i += 1

    def printfield(self):
        index = 0
        while index < len(self.field):
            self.field[index].image.draw(480, 310)
            index += 1

    def end(self):
        if len(self.hand) > 0:

            chosen = randint(0, len(self.hand) - 1)
            angle = atan2(160, 430 - 70 * chosen)
            x = 50 + 70 * chosen
            y = 470
            while abs(x - 480) > 40 and y > 310:
                clear_canvas()
                pane.draw(480, 270)
                self.printfield()
                self.printhand()
                self.printhp()
                myChar.printhp()
                myChar.printfield()
                myChar.printhand()
                cardback.draw(x, y)
                x += 40 * cos(angle)
                y -= 40 * sin(angle)
                delay(0.01)
                update_canvas()
            if len(self.field) > 0:
                self.field.remove(self.field[0])
            self.field.append(self.hand[chosen])
            self.hand.remove(self.hand[chosen])
        repaint()

    def printhp(self):

        font30.draw(465, 420, "%d" % self.hp, (255, 255, 255))


pane = load_image('./res/image/board.png')
cardback = load_image("./res/image/back.png")
myChar = Player()
myChar.createdeck()
ai = AI()
ai.createdeck()
font30 = load_font("./res/font/text.ttf", 30)
font50 = load_font("./res/font/text.ttf", 50)

def repaint():
    clear_canvas()
    pane.draw(480, 270)
    myChar.printhand()
    myChar.printfield()
    myChar.printhp()
    ai.printhand()
    ai.printfield()
    ai.printhp()
    update_canvas()


def fight(p1, p2):
    if len(p1.field) > 0 and len(p2.field) > 0:

        damage1 = p1.field[0].attack(p2.field[0])
        damage2 = p2.field[0].attack(p1.field[0])
        if damage1 < 0:
            p1.hp += damage1
            font30.draw(475,150,"%d" % damage1,(255,0,0))
        if damage2 < 0:
            p2.hp += damage2
            font30.draw(475,450,"%d" % damage2,(255,0,0))

    if len(p1.field)>0:
        p1.field.remove(p1.field[0])
    if len(p2.field)>0:
        p2.field.remove(p2.field[0])
    delay(1)
    repaint()
