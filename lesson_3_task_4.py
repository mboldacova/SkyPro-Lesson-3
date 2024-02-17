from turtle import *

screen = Screen()
screen.setup(800, 600)

t = Turtle()
t.speed(0)  

def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the bottom circle
draw_circle("light blue", 80, 0, -20)

# Draw the inside circle
draw_circle("white", 48, 0, -50)

# Draw the top circle
draw_circle("light blue", 60, 0, 100)

# Drawing left wing
t.color("light blue")

# Filling the shape of the left wing
t.begin_fill()

# Draw the oval for the lft wing
t.penup()
t.goto(-50, -20)  
t.pendown()

radius_x = 100
radius_y = 50

t.left(70)  
t.circle(radius_x, 90)  
t.left(90)  
t.circle(radius_y, 90)  

t.end_fill()

# Drawing right wing
t.color("light blue")

t.begin_fill()

# Draw the oval for the right wing
t.penup()
t.goto(10, 0) 
t.pendown()

radius_x = 100
radius_y = 50

t.left(20)  
t.circle(radius_x, 90)  
t.left(90)  
t.circle(radius_y, 90)  

t.end_fill()


# Drawing eyes
draw_circle("black", 5, -25, 120)
draw_circle("black", 5, 25, 120)

# Drawing the nose
t.penup()
t.goto(0, 100)
t.pendown()
t.color("orange")
t.begin_fill()
t.goto(10, 90)
t.goto(-10, 90)
t.goto(0, 100)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()