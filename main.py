import turtle
from PIL import Image, ImageTk
import tkinter as tk

# Set up the screen
wn = turtle.Screen()
wn.title("Happy Independence Day")
wn.colormode(255)
wn.bgcolor(1,200,50)
# wn.bgcolor("black")

# Create the turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(3)
flag_turtle.penup()
flag_turtle.shape("arrow")

# Function to draw a filled rectangle
def drawFillRectangle(x, y, length, width, color):
    flag_turtle.goto(x, y)
    flag_turtle.pendown()
    flag_turtle.color(color)
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(length)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    flag_turtle.penup()

# Function to draw a star
def drawStar(x, y, color, length):
    flag_turtle.goto(x, y)
    flag_turtle.setheading(-72)  # Adjusting the orientation
    flag_turtle.pendown()
    flag_turtle.begin_fill()
    flag_turtle.color(color)
    for _ in range(5):
        flag_turtle.forward(length)
        flag_turtle.right(144)
    flag_turtle.end_fill()
    flag_turtle.penup()

# Function to draw a filled circle
def drawCircle(x, y, color, radius):
    flag_turtle.goto(x, y - radius)  # Adjusting position to draw circle centered at (x, y)
    flag_turtle.color(color)
    flag_turtle.begin_fill()
    flag_turtle.circle(radius)
    flag_turtle.end_fill()

# Function to draw the moon (partially covered circle)
def drawMoon(x, y, color, radius):
    flag_turtle.up()
    flag_turtle.goto(x, y - radius)
    flag_turtle.color(color)
    flag_turtle.begin_fill()
    flag_turtle.circle(radius)
    flag_turtle.end_fill()

# Function to draw the green part of the flag
def drawGreen():
    x = -230
    y = 125
    color = 'dark green'
    drawFillRectangle(x, y, 280, 460, color)

# Function to draw the white stripe of the flag
def drawWhite():
    x = -230
    y = 125
    color = 'white'
    drawFillRectangle(x, y, 280, 130, color)

# Draw the star on the flag
def drawStarOnFlag():
    x = 70
    y = 15
    color = 'white'
    drawStar(x, y, color, 50)

# Draw the circle for the crescent moon
def drawCircleOnFlag():
    x = 45
    y = -20
    color = 'white'
    drawCircle(x, y, color, 80)

# Draw the overlapping circle to form the crescent moon
def drawMoonOnFlag():
    x = 75
    y = -20
    color = 'dark green'
    drawMoon(x, y, color, 70)

# Draw the flag
drawGreen()
drawWhite()
drawCircleOnFlag()
drawMoonOnFlag()
drawStarOnFlag()

# Write the title
flag_turtle.goto(0, 200)
flag_turtle.color("White")
flag_turtle.write("Happy Independence Day, Pakistan!", align="center", font=("Arial", 24, "bold"))

# Write "PAKISTAN ZINDABAD" at the bottom
flag_turtle.goto(0, -250)
flag_turtle.color("white")
flag_turtle.write("PAKISTAN ZINDABAD\n", align="center", font=("Arial", 20, "bold"))

# Hide the turtle and keep the window open
flag_turtle.hideturtle()
turtle.done()

# Function to display Quaid-e-Azam's photo using tkinter and PIL
def display_quaid_e_azam_photo():
    # Initialize tkinter
    root = tk.Tk()
    root.title("Quaid-e-Azam - Happy Independence Day")
    # Load the image
    img_path = r"E:new python\lib\site_pakages\PIL\quaid_e_azam.jpg" # Ensure the image file is in the same directory
    img = Image.open(img_path)
    img = img.resize((200, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # Create a label and add the image
    panel = tk.Label(root, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    # Add a text label
    text = tk.Label(root, text="Happy Independence Day, Pakistan! ", font=("Arial", 20, "bold"), fg="green")
    text.pack(side="bottom")

    # Keep the window open
    root.mainloop()

# Call the function to display Quaid-e-Azam's photo
display_quaid_e_azam_photo()

