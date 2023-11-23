import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0

# set up screen

window = turtle.Screen()
window.title('Snake')
window.bgcolor('#070B16')
window.setup(width=600, height=600)
window.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('#6CDD47')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('#ED3334')
food.penup()
food.goto(0, 100)

segments = []

# score board

sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('#EAFF88')
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write('SCORE: 0   HIGH SCORE: 0', align='center', font=('Arial', 24, 'bold'))

# Functions


def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    global x, y
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings

window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')

# Main Loop

while True:
    window.update()

    # check collisions with border area
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # hide the segments of body
        for segments in segments:
            segments.goto(1000, 1000)

        # clear the segments
        segments.clear()

        # reset the game
        score = 0
        delay = 0.1
        sc.clear()
        sc.write(f'SCORE: {score}', align='center', font=('Arial', 24, 'bold'))

    # check collision with food
    if head.distance(food) < 20:
        # move the food to random place
        x = random.randint(-285, 285)
        y = random.randint(-285, 250)
        food.goto(x, y)

        # add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('#6CDD47')
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001
        # increase the score
        score += 1

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write(f'SCORE: {score}   HIGH SCORE: {high_score}', align='center', font=('Arial', 24, 'bold'))

    # move the segments in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # move segments 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # hide segments
            for g in segments:
                g.goto(1000, 1000)
            segments.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write(f'SCORE: {score}   HIGH SCORE: {high_score}', align='center', font=('Arial', 24, 'bold'))

    time.sleep(delay)
