import turtle

# Set up the screen
sc = turtle.Screen()
sc.bgcolor("pink")
sc.setup(width=700, height=700)
turtle.title("Welcome to Turtle Window")

# Create turtle object
board = turtle.Turtle()
board.fillcolor("green")

# Begin filling the shape
board.begin_fill()

# Draw a decagon (10-sided polygon)
n = 10
for _ in range(n):
    board.forward(100)
    board.left(360 / n)

# End filling and finish
board.end_fill()
turtle.done()