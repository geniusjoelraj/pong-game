from turtle import Turtle
import time
import random

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pu()
        self.goto(position)
        self.xmove = 10
        self.ymove = 10
        self.var = 0.05

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)
        speed = self.var
        time.sleep(speed)
        

    def bounce(self):
        self.ymove *= -1

    def deflect(self):
        self.xmove *= -1
        self.ymove *= -1

    def respawn(self):
        self.goto(0, random.randint(-300, 300))
        self.xmove *= -1
        self.var = self.var/ 1000
