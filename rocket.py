from turtle import Turtle


class Rocket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("rocket.gif")
        self.penup()
        self.setpos(position)
        self.showturtle()

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def shoot(self):
        pass


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()

    def win(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!!", align="center", font=("Courier", 30, "normal"))