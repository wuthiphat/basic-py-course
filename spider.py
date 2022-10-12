import turtle
t = turtle.Pen()
t.shape('turtle')
t.speed(200)
t.left(45)
def one():
    for i in range(8):
        t.forward(100)
        t.penup()
        t.backward(100)
        t.pendown()
        t.left(45)
def two():
    for i in range(80):
        t.forward(1+i)
        t.left(45)
one()
two()
