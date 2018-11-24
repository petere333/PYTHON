from pico2d import *

open_canvas(960, 540)
image1 = load_image("./res/image/1,1.png")
image2 = load_image("./res/image/1,3.png")
image3 = load_image("./res/image/1,5.png")
image4 = load_image("./res/image/2,1.png")
image5 = load_image("./res/image/2,3.png")
image6 = load_image("./res/image/2,7.png")
image7 = load_image("./res/image/3,2.png")
image8 = load_image("./res/image/3,4.png")
image9 = load_image("./res/image/4,1.png")
image10 = load_image("./res/image/4,5.png")
image11 = load_image("./res/image/5,1.png")
image12 = load_image("./res/image/5,2.png")
image13 = load_image("./res/image/5,4.png")
image14 = load_image("./res/image/5,6.png")
image15 = load_image("./res/image/5,9.png")
image16 = load_image("./res/image/6,3.png")
image17 = load_image("./res/image/6,7.png")
image18 = load_image("./res/image/6,10.png")
image19 = load_image("./res/image/7,4.png")
image20 = load_image("./res/image/7,7.png")
image21 = load_image("./res/image/7,14.png")
image22 = load_image("./res/image/9,5.png")
image23 = load_image("./res/image/10,10.png")


attacks = [1,1,1,2,2,2,3,3,4,4,5,5,5,5,5,6,6,6, 7,7,7, 9,10]
hps =     [1,3,5,1,3,7,2,4,1,5,1,2,4,6,9,3,7,10,4,7,14,5,10]
images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10,
          image11, image12, image13, image14, image15, image16,image17,image18,image19,
          image20, image21, image22, image23]

class Card:

    def __init__(self):
        self.atk = 0
        self.hp = 0
        self.image = load_image('./res/image/error.png')
        self.index = 0

    def get(self, index):
        self.atk = attacks[index]
        self.hp = hps[index]
        self.image = images[index]
        self.index=index

    def attack(self, enemy):
        return self.hp-enemy.atk
