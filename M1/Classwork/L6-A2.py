import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("orange")

# Create turtle object
board = turtle.Turtle()

# Draw first triangle
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

# Reposition for second triangle
board.penup()
board.right(150)
board.forward(55)
board.pendown()

# Draw second triangle
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

# Finish drawing
turtle.done()