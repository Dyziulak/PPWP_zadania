import turtle

def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
    win.title("Tess & Bob")
    
    # Utwórz obiekt tess klasy Turtle i ustaw jego atrybuty
    tess = turtle.Turtle() 
    tess.shape("turtle")
    tess.color("hotpink") 
    tess.pensize(5) 
    
    # Utwórz obiekt bob klasy Turtle i ustaw jego atrybuty
    bob = turtle.Turtle() 
    bob.shape("turtle")
    
    # tess rysuje trójkat
    tess.forward(180)
    tess.left(120) 
    tess.forward(180) 
    tess.left(120) 
    tess.forward(180) 
    tess.left(120) 
    
    tess.right(180) 
    tess.penup()
    tess.forward(80) 
    
    # bob rysuje kwadrat
    bob.forward(150)
    bob.left(90) 
    bob.forward(150) 
    bob.left(90) 
    bob.forward(150) 
    bob.left(90) 
    bob.forward(150) 
    bob.left(90) 

    win.mainloop()

main()

