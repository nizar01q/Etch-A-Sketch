from turtle import Turtle, Screen


screen = Screen()
kratos = Turtle()


def move_forward():
    kratos.forward(10)


def move_backwards():
    kratos.forward(-10)


def right():
    kratos.right(10)


def left():
    kratos.left(10)


def clear():
    kratos.clear()
    kratos.penup()
    kratos.home()
    kratos.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)





















screen.exitonclick()