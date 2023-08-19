from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(position)
        self.write(self.score, align='center', font=('Courier', 100, 'normal'))
        
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align='center', font=('Courier', 100, 'normal'))