def draw_house(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.color("#DEB887")
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(180)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.color("#B22222")
    pen.begin_fill()
    pen.goto(x, y + 100)
    pen.goto(x + 90, y + 170)
    pen.goto(x + 180, y + 100)
    pen.goto(x, y + 100)
    pen.end_fill()

    pen.penup()
    pen.goto(x + 70, y)
    pen.color("#654321")
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
            pen.forward(40)
            pen.left(90)
            pen.forward(60)
            pen.left(90)
    pen.end_fill()

    def window(wx, wy):
            pen.penup()
            pen.goto(wx,wy)
            pen.color("#ADD8E6")
            pen.begin_fill()
            pen.pendown()
            for _ in range(4):
                pen.forward(30)
                pen.left(90)
            pen.end_fill()

    window(x + 20, y + 40)
    window(x + 130, y + 40)

draw_house(-90,-180)

turtle.done()