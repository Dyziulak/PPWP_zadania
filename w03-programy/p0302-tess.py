import turtle

def main():
  win = turtle.Screen()
  win.bgcolor("lightgreen") 
  win.title("Hello, Tess!") 
  
  tess = turtle.Turtle()
  
  tess.color("blue")
  tess.pensize(3)
  tess.forward(200)
  tess.left(120)
  tess.forward(200)
  win.mainloop()

main()
