import turtle

def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
  
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")
    tess.penup()
  
    size = 20
    for j in range(30):
        tess.stamp()
        size = size + 3
        tess.forward(size)
        tess.right(24)
    
    win.mainloop()

main()

