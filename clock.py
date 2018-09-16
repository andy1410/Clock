from turtle import Turtle
from datetime import datetime
from time import sleep

clock_turtle = Turtle()
hour_turtle = Turtle()
minute_turtle = Turtle()
second_turtle = Turtle()

turtles = [clock_turtle, hour_turtle, minute_turtle, second_turtle]

for turtle in turtles:
    turtle.speed(0)
    turtle.hideturtle()


def make_clock():
    clock_turtle.penup()
    clock_turtle.color('#37474F', '#ECEFF1')

    # Making Circle
    clock_turtle.forward(300)
    clock_turtle.left(90)
    clock_turtle.pendown()
    clock_turtle.begin_fill()
    clock_turtle.circle(300)
    clock_turtle.end_fill()
    clock_turtle.penup()

    clock_turtle.home()
    clock_turtle.left(90)

    for i in range(0, 60):
        clock_turtle.forward(250)
        if i % 5 == 0:
            # 5 minutes complete
            clock_turtle.pensize(10)
            clock_turtle.pendown()
            clock_turtle.forward(30)
            clock_turtle.back(30)
            clock_turtle.penup()

        else:
            clock_turtle.pensize(2)
            clock_turtle.forward(10)
            clock_turtle.pendown()
            clock_turtle.forward(20)
            clock_turtle.back(20)
            clock_turtle.penup()
            clock_turtle.back(10)

        clock_turtle.back(250)
        clock_turtle.right(6)

    clock_turtle.home()


def setup_hour_hand():
    hour_turtle.pensize(10)
    hour_turtle.color('#212121')
    hour_turtle.home()
    hour_turtle.left(90)


def setup_minute_hand():
    minute_turtle.pensize(5)
    minute_turtle.color('#424242')
    minute_turtle.home()
    minute_turtle.left(90)


def setup_second_hand():
    second_turtle.home()
    second_turtle.left(90)
    second_turtle.pensize(2)
    second_turtle.color('#616161')


def get_current_time():
    now = datetime.now()
    seconds = now.second * 6
    minutes = now.minute * 6 + seconds // 60
    hour = (now.hour % 12) * 30 + minutes // 12
    return hour, minutes, seconds


def start_clock():
    make_clock()
    setup_hour_hand()
    setup_minute_hand()
    setup_second_hand()

    hours, minutes, seconds = get_current_time()

    old_hours = -1
    old_minutes = -1

    for turtle_ in turtles:
        turtle_.hideturtle()
        turtle_.hideturtle()

    while True:
        start_time = datetime.now()
        if hours != old_hours:
            hour_turtle.undo()
            hour_turtle.undo()
            hour_turtle.right(hours)
            hour_turtle.forward(100)

        if minutes != old_minutes:
            minute_turtle.undo()
            minute_turtle.undo()
            minute_turtle.right(minutes)
            minute_turtle.forward(200)

        second_turtle.undo()
        second_turtle.undo()
        second_turtle.undo()
        second_turtle.right(seconds)
        second_turtle.back(20)
        second_turtle.forward(250)

        old_minutes = minutes
        old_hours = hours

        seconds += 6

        if seconds % 60 == 0:
            minutes += 1

        if minutes % 12 == 0 and old_minutes != minutes:
            hours += 1

        seconds %= 360
        minutes %= 360
        hours %= 360
        end_time = datetime.now()
        time_delta = end_time - start_time
        sleep_seconds = 1 - time_delta.microseconds/1000000
        sleep(sleep_seconds)


if __name__ == '__main__':
    try:
        start_clock()
    except:
        pass