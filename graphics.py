#Created By Rabia Alhaffar In 13/January/2020
#Graphics Module For Blueberry,In Development!!!
#NOTES: It Uses turtle Module So It Requires Python 2.5+
import turtle,random
from turtle import *
from random import *
blueberry = turtle
def init(h,w,t):
      window = Screen()  
      window.setup(width=w , height=h ) 
      blueberry = turtle
      windowheight = blueberry.window_height()
      windowwidth = blueberry.window_width()
      blueberry.speed(0) 
      blueberry.hideturtle()
      blueberry.title(t)
def forward(px):
  blueberry.fd(px)
    
def backward(px): 
  blueberry.bk(px)
    
def clear(): 
  blueberry.clear()

def go(x,y): 
  blueberry.goto(x,y)
    
def translate(x,y):
  blueberry.penup()
  blueberry.setx(x) 
  blueberry.sety(y)
  blueberry.pendown()
    
def color(fill,stroke):	
  blueberry.pencolor(stroke,fill)
    
def reset():
  blueberry.reset()
    
def pixel(x,y,s,color):
  blueberry.penup()
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.dot(s,color)
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()
    
def flashback():
  blueberry.undo()
    
def strokecolor(c):
  blueberry.pencolor(c)

def fillcolor(c):
  blueberry.fillcolor(c)

def color(fill,stroke):
  blueberry.color(stroke,fill)
  
def colorbg(c):
  blueberry.bgcolor(c)
    
def gdshape(s):
  blueberry.shape(s)
    
def turnright(angle):
  blueberry.right(angle)

def turnleft(angle):
  blueberry.left(angle) 

def circle(x,y,r,fill,stroke):
  blueberry.color(stroke,fill)
  blueberry.penup()  
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.begin_fill()
  blueberry.circle(r)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()
  
def text(x,y,text,move,align,font):
  blueberry.penup()
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.write(text,move,align,font)
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()
  
def bgimg(img_src):
  blueberry.bgpic(img_src)

def wait(s):
  blueberry.delay(s)

#NOTES: update() Here Used Last Of Game Code,Also Use clear() At Begining To Update Game Content!!!
def update():
  blueberry.mainloop()

def beginfill():
  blueberry.begin_fill()

def endfill():
  blueberry.end_fill()

def focus():
  blueberry.listen()

def triangle(x,y,a,b,c,fill,stroke):
  blueberry.penup()
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.pendown()
  blueberry.begin_fill()
  blueberry.goto(a,b)
  blueberry.goto(b,c)
  blueberry.goto(c,a)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()

def call(gamefunction,fps):
  blueberry.ontimer(gamefunction,fps)

def rotate(angle):
  blueberry.tilt(angle)

def setangle(angle):
  blueberry.settiltangle(angle)

def resettilting(angle):
  blueberry.tilt(0)

def square(x,y,size,fill,stroke):
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.color(stroke,fill)
  blueberry.fillcolor(fill)
  blueberry.pencolor(stroke)
  blueberry.begin_fill()
  x = x + size
  blueberry.goto(x,y)
  y = y - size
  blueberry.goto(x,y)
  x = x - size
  blueberry.goto(x,y)
  y = y + size
  blueberry.goto(x,y)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()

def rect(x,y,h,w,fill,stroke): 
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.color(stroke,fill)
  blueberry.fillcolor(fill)
  blueberry.pencolor(stroke)
  blueberry.begin_fill()
  x = x + w
  blueberry.goto(x,y)
  y = y - h
  blueberry.goto(x,y)
  x = x - w
  blueberry.goto(x,y)
  y = y + h
  blueberry.goto(x,y)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()

def line(x1,y1,x2,y2,stroke):
      blueberry.color(stroke)
      blueberry.penup()
      blueberry.setx(x1)
      blueberry.sety(y1)
      blueberry.pendown()
      blueberry.pencolor(stroke)
      blueberry.goto(x2,y2)
      blueberry.penup()
      blueberry.home()
      blueberry.pendown()
      
def poly(points,fill,stroke):
    p = len(points)
    blueberry.color(stroke,fill)
    blueberry.penup()
    blueberry.setx(points[0][0])
    blueberry.sety(points[0][1])
    blueberry.pendown()
    blueberry.begin_fill()
    blueberry.pencolor(stroke)
    blueberry.fillcolor(fill)
    for x in range(p):
          blueberry.pencolor(stroke)
          blueberry.fillcolor(fill)
          blueberry.goto(points[x][0],points[x][1])
    blueberry.end_fill()
    blueberry.penup()
    blueberry.home()
    blueberry.pendown()
    
def polysides(x,y,sides,size,fill,stroke):
      blueberry.color(stroke,fill)
      blueberry.penup()
      blueberry.setx(x)
      blueberry.sety(y)
      blueberry.pendown()
      blueberry.begin_fill()
      blueberry.pencolor(stroke)
      blueberry.fillcolor(fill)
      a = 360 / sides
      for s in range(sides):
            blueberry.forward(size)
            blueberry.left(a)
      blueberry.end_fill()
      blueberry.penup()
      blueberry.home()
      blueberry.pendown()
