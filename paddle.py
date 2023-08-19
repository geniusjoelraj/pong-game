from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position  = (position)
        self.color('white')
        self.shape('square')
        self.shapesize(1, 6)
        self.pu()
        self.speed('fastest')
        self.goto(self.position)
        self.seth(90)

    def up(self):
        if self.ycor() < 320:
            self.fd(20)
    
    def down(self):
        if self.ycor() > -320:
            self.bk(20)

