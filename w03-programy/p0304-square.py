import turtle

def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen") 
    win.title("Kwadrat") 
  
    bob = turtle.Turtle()
    bob.color("blue")
    bob.pensize(3)

    # bob rysuje kwadrat
    for j in range(4):
        bob.forward(150)
        bob.left(90)
    
    win.mainloop()

main()
