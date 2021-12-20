import turtle
import time


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_tl():
    turtle.circle(100)
    gotoxy(0, 35)
    turtle.circle(20)
    gotoxy(0, 85)
    turtle.circle(20)
    gotoxy(0, 135)
    turtle.circle(20)


class TrafficLight:
    __color = 'Чёрный'

    def running(self):
        while True:
            gotoxy(0, 135)
            draw_circle(20, 'red')
            time.sleep(7)
            draw_circle(20, 'white')
            gotoxy(0, 85)
            draw_circle(20, 'yellow')
            time.sleep(2)
            draw_circle(20, 'white')
            gotoxy(0, 35)
            draw_circle(20, 'green')
            time.sleep(7)
            draw_circle(20, 'white')


turtle.speed(0)
draw_tl()
tl = TrafficLight()
tl.running()
