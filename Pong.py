import turtle 
from turtle import *
bgcolor("black")
wn = turtle.Screen() #opens a window
wn.title("Pong by Shashwat") #title of the project
wn.setup(width = 800 , height = 600) #size of the window
wn.tracer (0) #stops the window from updating so we have to manually update it (makes game faster)


# Paddle A
paddle_a = turtle.Turtle()#module name and the class name
paddle_a.speed(0) #speeds down everything
paddle_a.shape("square") #shape
paddle_a.color("white") #colour of the object
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # size of the object
paddle_a.penup() #so that lines are not drawn
paddle_a.goto(-350, 0)#specification of the sstarting point


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1 ,stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25
#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#Keyboard Binding
wn.listen() #listens to the key board input
wn.onkeypress(paddle_a_up, "w")  #to move pad up
wn.onkeypress(paddle_a_down, "s")  #----""---- down
wn.onkeypress(paddle_b_up, "Up")  
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while True:
    wn.update () #every time the loop runs it updates the screen
    # Moving the Ball
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
    elif ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1

