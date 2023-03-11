import turtle 

bob = turtle.Turtle()

# bob.forward(100)
# bob.left(45)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)

bob.color("blue", "cyan")
bob.color("red", "yellow")



bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()


bob.penup()
bob.forward(150)
bob.pendown()

bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()




turtle.done()