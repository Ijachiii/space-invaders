from turtle import Turtle


class EvilRocket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.shape("evil.gif")
        self.color("blue")
        self.penup()
        self.setpos(position)
        self.showturtle()

    def shoot(self):
        pass
