import turtle

screen = turtle.Screen()
screen.setup(width=1000,height=650)
screen.bgcolor("#7BE5F8")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

pen.penup()
pen.goto(320,200)
pen.color("#FFD700")
pen.begin_fill()
pen.pendown()
pen.circle(60)
pen.end_fill()

def draw_mountain(x, y, width, height, color):
    pen.penup()
    pen.goto(x,y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    pen.goto(x + width / 2, y + height)
    pen.goto(x + width, y)
    pen.goto(x, y)
    pen.end_fill()

draw_mountain(-500, -100, 350, 220, "#4B6B3F")
draw_mountain(-250, -100, 400, 270, "#6B8E23")
draw_mountain(0, -100, 350, 250, "#4C5A32")
draw_mountain(250, -100, 400, 230, "#556B2F")

pen.penup()
pen.goto(-500, -100)
pen.color("#6bd66b")
pen.begin_fill()
pen.pendown()
pen.goto(500, -100)
pen.goto(500, -300)
pen.goto(-500, -300)
pen.goto(-500, -100)
pen.end_fill()

pen.penup()
pen.goto(-500, -160)
pen.color("#696969")
pen.begin_fill()
pen.pendown()
pen.goto(500, -160)
pen.goto(500, -210)
pen.goto(-500, -210)
pen.goto(-500, -160)
pen.end_fill()

pen.penup()
pen.goto(-500, -210)
pen.color("#1E90FF")
pen.begin_fill()
pen.pendown()
pen.goto(500, -210)
pen.goto(500, -270)
pen.goto(-500, -270)
pen.goto(-500, -210)
pen.end_fill()

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

def draw_trees(x, y, scale=1.0):
     pen.penup()
     pen.goto(x, y)
     pen.color("saddle brown")
     pen.begin_fill()
     pen.pendown()
     for _ in range(2):
          pen.forward(15 * scale)
          pen.left(90)
          pen.forward(50 * scale)
          pen.left(90)
     pen.end_fill()

     pen.penup()
     pen.goto(x - 20 * scale, y + 50 * scale)
     pen.color("forest green")
     pen.begin_fill()
     pen.pendown()
     for _ in range(3):
          pen.forward(55 * scale)
          pen.left(120)
     pen.end_fill()

draw_trees(-300, -180, 1.3)
draw_trees(-240, -180, 1.1)
draw_trees(200, -180, 1.2)
draw_trees(260,-180, 1.0)

pen.penup()

pen.goto(-400, 290)
pen.color("blue")
pen.write("Made by ayat", align="center", font=("Arial", 18,"bold"))

turtle.done()