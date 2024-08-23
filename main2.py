# Quiad e Azam photo display
import turtle as tur
tur.Turtle()
tur.Screen()
tur.title("Happy Independence Day!")
#title 
tur.goto(0, 200)

tur.color("White")
tur.write("Happy Independence Day, Pakistan!", align="center", font=("Arial", 24, "bold"))

tur.colormode(255)
tur.bgcolor(10,180,10)
tur.bgpic("Quiad.gif") 

# Write "PAKISTAN ZINDABAD" at the bottom
tur.goto(0, -250)
tur.color("white")
tur.write("PAKISTAN ZINDABAD", align="center", font=("Arial", 20, "bold"))
tur.hideturtle()

tur.done()