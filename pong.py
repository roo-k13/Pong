import turtle

# Window settings
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen_width = 1280
screen_height = 760
screen.setup(screen_width, screen_height)
screen.tracer(0)

# Shared paddle properties
speed = 0
shape = "square"
color = "white"
width = 5
length = 1
y_position = 0
x_position = 600

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(speed)
paddle_a.shape(shape)
paddle_a.color(color)
paddle_a.shapesize(width, length)
paddle_a.penup()
paddle_a.goto(x_position, y_position)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(speed)
paddle_b.shape(shape)
paddle_b.color(color)
paddle_b.shapesize(width, length)
paddle_b.penup()
paddle_b.goto(-x_position, y_position)

# Ball

# Main loop
while True:
    screen.update()
