#import turtle
#colors = ["green","yellow", "red", "black"]
#sketch = turtle.pen()
#turtle.bgcolor("purple")
#for i in range(50):
    #sketch.pencolor(colors[i%6])
   # sketch.width(i/90+1)
   # sketch.forward(i)
   # sketch.left(20)

import turtle
colors = ["pink", "yellow", "blue", "green", "white", "red"]
sketch = turtle.Pen()
turtle.bgcolor("blue")
for i in range(100):
        sketch.pencolor(colors[i % 6])
        sketch.width(i / 700 + 1)
        sketch.forward(i)
        sketch.left(50)