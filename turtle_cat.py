import turtle
import math

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("black")

    cursor = turtle.Turtle() # Cursor
    cursor.shape("turtle")
    cursor.color("white")
    cursor.speed(0)
    cursor.pensize(10)

    # Draw the head

    movePenY(cursor, -150)
    cursor.circle(150)

    # Draw the nose

    movePenY(cursor, -20)
    cursor.circle(20)

    # Draw the mouth

    movePen(cursor, -100, -20)
    cursor.right(90)
    cursor.circle(50, 180)
    cursor.left(180)
    cursor.circle(50, 180)
    
    # Draw the eyes

    eyeSpacingX = 30
    eyePosY = 40
    eyeRadius = 30
    
    # Right eye

    movePen(cursor, eyeSpacingX, eyePosY)
    cursor.right(180)
    cursor.circle(eyeRadius, -180)

    # Left eye

    movePen(cursor, -eyeSpacingX, eyePosY)
    cursor.circle(eyeRadius, 180)

    cursor.speed(3)

    # Draw the tongue

    pos = positionAlongCircle(0, 0, 150, 90)
    movePen(cursor, pos[0], pos[1])
    cursor.forward(100)
    print( pos )


    window.exitonclick()

def movePen(cursor, x, y):
    cursor.penup()
    cursor.setposition(x, y)
    cursor.pendown()

def movePenX(cursor, x):
    cursor.penup()
    cursor.setx(x)
    cursor.pendown()

def movePenY(cursor, y):
    cursor.penup()
    cursor.sety(y)
    cursor.pendown()

def positionAlongCircle(x, y, radius, angle):
    radians = math.radians(angle)
    return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

draw_shape()
