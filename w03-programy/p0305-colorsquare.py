import turtle

def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen") 
    win.title("Kwadrat") 
  
    bob = turtle.Turtle()
    bob.pensize(3)

    # bob rysuje kolorowy kwadrat
    for c in ["yellow", "red", "purple", "blue"]:
        bob.color(c)
        bob.forward(150)
        bob.left(90)
  
    win.mainloop()

main()
