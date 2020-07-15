import turtle 
from turtle import *
bgcolor("black")
wn = turtle.Screen() #opens a window
wn.title("Pong by Shashwat") #title of the project
wn.setup(width = 800 , height = 600) #size of the window
wn.tracer (0) #stops the window from updating so we have to manually update it (makes game faster)





# Main game loop
while True:
    wn.update () #every time the loop runs it updates the screen


