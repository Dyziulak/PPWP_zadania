import math, turtle

def main():
    win = make_window("khaki2", "Kolorowe koła")
    bob = make_turtle("blue", 3, 0)
    tess = make_turtle("red", 2, 0)
    alex = make_turtle("green", 1, 0)
    draw_wheel(bob, 300, 720)
    draw_wheel(tess, 200, 720)
    draw_wheel(alex, 100, 720)
    win.mainloop()

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, pensize, speed):
    tom = turtle.Turtle()
    tom.color(color)
    tom.pensize(pensize)
    tom.speed(speed)
    return tom
    
def jumpto(tom, x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()

def draw_wheel(tom, radius, n):
    tom.begin_fill()
    jumpto(tom, 0, -radius)
    length = (2 * math.pi * radius) / n
    for j in range(n):
        tom.left(360 / n)
        tom.forward(length)
    tom.end_fill()
    tom.hideturtle()

main()
