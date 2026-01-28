import turtle

# Create turtle and screen
t = turtle.Turtle()
s = turtle.Screen()

# Set background and turtle settings
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

while True:
  
  for x in range(0,200):  # 0..199
    t.pencolor(colors[x%len(colors)])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)
  t.right(239)

  for x in range(200, 0, -1):  # 200..1
        t.pencolor('black')
        t.width(x/100 + 10)
        t.forward(x)
        t.right(59)
