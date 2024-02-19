import turtle

turtle.title("My	Python	Turtle	Journey")
turtle.bgcolor("pink") #
t=turtle.Turtle()
n=100
while	n	>=	10:
    t.begin_fill()
    t.circle(n)
    t.pensize(2)
    t.pencolor("black")
    if	(n==20	or	n==40	or	n==60		or	n==80	or	n==100):
        t.fillcolor("red")
        n = n - 10
    else:
        t.pencolor("blue")
        t.fillcolor("blue")
        n = n - 10
    t.end_fill()

turtle.mainloop()