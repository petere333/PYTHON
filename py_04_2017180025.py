import turtle as t
import random as r

def tree(direction,level):
    temp=0
    t.pensize(10-level)
    if(level<=5):
        t.pencolor((100+level*30,0,0))
        temp=r.random()*10
    elif(level<=9 and level>5):
        t.pencolor((0,100+(level-6)*30,0))
    if(direction==1):
        t.left(20)
    elif(direction==2):
        t.right(20)

    t.pendown()
    t.forward(60-(level-1)*4)
    
    if(level<9):
        if(temp>6):
            t.pensize(2)
            t.pencolor((100,100,100))
            t.left(50)
            t.forward(20)
            t.left(180)
            t.forward(20)
            t.left(180)
            
            
            t.right(100)
            t.forward(20)
            t.left(180)
            t.forward(20)
            t.left(180)
            
            t.pensize(10-level)
            t.left(50)
            if(level<=5):
                t.pencolor((100+level*30,0,0))
            elif(level<=9 and level>5):
                t.pencolor((0,100+(level-6)*30,0))

        tree(1,level+1)

        t.penup()
        t.left(180)
        t.forward(60-level*4)
        t.left(180)
        t.right(20)
        
        tree(2,level+1)
        t.left(180)
        t.penup()
        t.forward(60-level*4)
        t.left(180)
        t.left(20)
        

t.colormode(255)
t.pencolor((0,0,0))
t.pensize(9)
t.penup()
t.goto(0,-100)
t.left(90)
t.pendown()
t.forward(60)

tree(1,1)
t.penup()
t.left(180)
t.forward(60)
t.left(180)
t.right(20)
tree(2,1)
t.penup()
t.left(180)
t.forward(60)
t.left(180)
