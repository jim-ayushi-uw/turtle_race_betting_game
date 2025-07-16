from turtle import Turtle, Screen

tim = Turtle()
jen = Turtle()
jen.color("purple")
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(50)

def move_counterclock():
    tim.left(90)

def move_clockwise():
    tim.right(90)
def clear_screen():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()