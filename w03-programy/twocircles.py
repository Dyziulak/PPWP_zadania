import math, turtle

def main():
    win = make_window("khaki2", "Dwa okręgi")
    bob = make_turtle("blue", 3, 0)
    tess = make_turtle("red", 2, 0)
    draw_circle(bob, 300, 720)
    draw_circle(tess, 200, 720)
    win.mainloop()

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, pensize, speed):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(pensize)
    t.speed(speed)
    return t
    
def draw_circle(t, radius, n):
    jumpto(t, 0, -radius)
    length = (2 * math.pi * radius) / n
    for j in range(n):
        t.left(360 / n)
        t.forward(length)

def jumpto(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
main()
