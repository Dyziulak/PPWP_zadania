import turtle


def main():
    w = turtle.Screen(); 
    w.bgcolor("lightgreen")

    tess = turtle.Turtle(); 
    tess.pensize(3)
    tess.speed(0)
    
    for length in range(20, 220, 10):
        draw_multicolor_square(tess, length)
        tess.forward(10); 
        tess.right(18)
    w.mainloop()


def draw_multicolor_square(t, length):
    for c in ["red", "purple", "hotpink", "blue"]:
        t.color(c)
        t.forward(length)
        t.left(90)


main()
