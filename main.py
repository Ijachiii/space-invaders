from turtle import Turtle, Screen
from rocket import Rocket, Score
from evil_ship import EvilRocket


# setting up screen
screen = Screen()
screen.setup(width=750, height=600)
screen.bgpic("space.gif")
screen.addshape("rocket.gif")
screen.addshape("evil.gif")
rocket = Rocket((0, -235))
score = Score()
evil_list = []


# creating bullet
bullet = Turtle()
bullet.shapesize(stretch_wid=1, stretch_len=1.5)
bullet.penup()
bullet.color("red")
bullet.hideturtle()
bullet.setheading(90)
bullet_state = "ready"
bullet_speed = 50


# defining shooting function
def fire():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        new_y = rocket.ycor() + 30
        bullet.setpos(rocket.xcor(), new_y)
        bullet.showturtle()


x = 0
y = 235
for i in range(1, 6):
    evil = EvilRocket((x, y))
    x += 80
    evil_list.append(evil)

x = -80
y = 235
for i in range(1, 5):
    evil = EvilRocket((x, y))
    x -= 80
    evil_list.append(evil)


# associating keyboard controls
screen.onkey(rocket.go_left, "Left")
screen.onkey(rocket.go_right, "Right")
screen.onkey(fire, "space")
screen.listen()

game = True
while game:
    screen.update()
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 295:
        bullet.hideturtle()
        bullet.setpos(0, -235)
        bullet_state = "ready"

    for alien in evil_list:
        if bullet.distance(alien) < 30:
            evil_list.remove(alien)
            bullet.hideturtle()
            alien.hideturtle()
            alien.setpos(0, 300)
            bullet.setpos(0, -235)
            bullet_state = "ready"

    if len(evil_list) == 0:
        score.win()
        game = False

screen.mainloop()
