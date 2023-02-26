from turtle import Turtle

class Name(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_state(self,state_name,cors):
        self.goto(cors)
        self.write(state_name)
