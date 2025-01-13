import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# screen 
sc = turtle.Screen()
sc.title("Snake Game")
sc.bgcolor("pink")
sc.setup(width=700, height=700)
sc.tracer(0)

# snake head 
jw = turtle.Turtle()
jw.shape("square")
jw.color("black")
jw.penup()
jw.goto(0, 0)
jw.direction = "Stop"

# food 
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# pen score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# movement
def up():
    if jw.direction != "down":
        jw.direction = "up"

def down():
    if jw.direction != "up":
        jw.direction = "down"

def left():
    if jw.direction != "right":
        jw.direction = "left"

def right():
    if jw.direction != "left":
        jw.direction = "right"

def move():
    if jw.direction == "up":
        jw.sety(jw.ycor() + 20)
    if jw.direction == "down":
        jw.sety(jw.ycor() - 20)
    if jw.direction == "right":
        jw.setx(jw.xcor() + 20)
    if jw.direction == "left":
        jw.setx(jw.xcor() - 20)

# bindings
sc.listen()
sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")

# game loop
segments = []

while True:
    sc.update()

    # border collision
    if jw.xcor() > 340 or jw.xcor() < -340 or jw.ycor() > 340 or jw.ycor() < -340:
        time.sleep(1)
        jw.goto(0, 0)
        jw.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

    # food collision
    if jw.distance(food) < 20:
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

    # move segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = jw.xcor()
        y = jw.ycor()
        segments[0].goto(x, y)

    move()

    # self-collision
    for segment in segments:
        if segment.distance(jw) < 20:
            time.sleep(1)
            jw.goto(0, 0)
            jw.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("candara", 24, "bold"))

    time.sleep(delay)
