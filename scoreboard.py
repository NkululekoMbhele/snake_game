from turtle import Turtle 


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score {self.score}", True, "center", ("Arial", 10, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, "center", ("Arial", 10, "normal"))
        
    
    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       