#Created By Rabia Alhaffar In 13/January/2020
#Graphics Module For Blueberry,In Development!!!
#NOTES: It Uses turtle Module So It Requires Python 2.5+
import turtle,random
from turtle import *
from random import *
blueberry = turtle
def init(w,h,t):
      if h == None: h = 600
      if w == None: w = 600
      if t == None: t = "GAME"
      bwindow = Screen()  
      bwindow.setup(width=w , height=h ) 
      blueberry = turtle
      windowheight = blueberry.window_height()
      windowwidth = blueberry.window_width()
      bturtle = blueberry.Turtle()
      blueberry.speed(0) 
      blueberry.hideturtle()
      blueberry.title(t)
def forward(px):
      if px == None: px = 0
      blueberry.fd(px)
    
def backward(px):
      if px == None: px = 0
      blueberry.bk(px)
    
def clear():
      blueberry.clear()

def go(x,y):
      if x == None: x = 0
      if y == None: y = 0
      blueberry.goto(x,y)
    
def translate(x,y):
  if x == None: x = 0
  if y == None: y = 0
  blueberry.penup()
  blueberry.setx(x) 
  blueberry.sety(y)
  blueberry.pendown()
    
def color(fill,stroke):
      if fill == None: fill = "black"
      if stroke == None: stroke = "black"
      blueberry.pencolor(stroke,fill)
    
def reset():
      blueberry.reset()
    
def pixel(x,y,s,color):
  if x == None: x = 0
  if y == None: y = 0
  if s == None: s = 1
  blueberry.penup()
  blueberry.pensize(1)
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
  if c == None: c = "black"
  blueberry.pencolor(c)

def fillcolor(c):
  if c == None: c = "black"
  blueberry.fillcolor(c)

def color(fill,stroke):
  blueberry.color(stroke,fill)
  
def colorbg(c):
  if c == None: c = "black"
  blueberry.bgcolor(c)
    
def gdshape(s):
  blueberry.shape(s)
    
def turnright(angle):
  if angle == None: angle = 0
  blueberry.right(angle)

def turnleft(angle):
  if angle == None: angle = 0
  blueberry.left(angle) 

def circle(x,y,r,fill,stroke):
  if x == None: x = 0
  if y == None: y = 0
  if r == None: r = 1
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
  blueberry.color(stroke,fill)
  blueberry.penup()  
  blueberry.pensize(1)
  blueberry.setx(x)
  blueberry.sety(y)
  blueberry.pendown()
  blueberry.begin_fill()
  blueberry.circle(r)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()
  
def text(x,y,text,move,align,fonttype,fontsize,fontmode):
  if x == None: x = 0
  if y == None: y = 0
  if text == None: text = ""
  if move == None: move = False
  if align == None: align = "left"
  if fontsize == None: fontsize = 8
  if fonttype == None: fonttype = "arial"
  if fontmode == None: fontmode = "noraml"
  font = (fonttype,fontsize,fontmode)
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
  blueberry.update()

def beginfill():
  blueberry.begin_fill()

def endfill():
  blueberry.end_fill()

def focus():
  blueberry.listen()
 
def tri(x,y,a,b,c,fill,stroke):
  if x == None: x = 0
  if y == None: y = 0
  if a == None: a = 0
  if b == None: b = 0
  if c == None: c = 0
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
  blueberry.penup()
  blueberry.pensize(1)
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

def triangle(x1,y1,x2,y2,x3,y3,fill,stroke):
  if x1 == None: x1 = 0
  if y1 == None: y1 = 0
  if x2 == None: x2 = 0
  if y2 == None: y2 = 0
  if x3 == None: x3 = 0
  if y3 == None: y3 = 0
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
  blueberry.penup()
  blueberry.pensize(1)
  blueberry.setx(x1)
  blueberry.sety(y1)
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.pendown()
  blueberry.begin_fill()
  blueberry.goto(x2,y2)
  blueberry.goto(x3,y3)
  blueberry.goto(x1,y1)
  blueberry.end_fill()
  blueberry.penup()
  blueberry.home()
  blueberry.pendown()

def call(gamefunction,fps):
  blueberry.ontimer(gamefunction,fps)

def rotate(angle):
  if angle == None: angle = 0
  blueberry.tilt(angle)

def setangle(angle):
  if angle == None: angle = 0
  blueberry.settiltangle(angle)

def resettilting():
  blueberry.tilt(0)

def square(x,y,size,fill,stroke):
  if x == None: x = 0
  if y == None: y = 0
  if size == None: size = 1
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.pensize(1)
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

def rect(x,y,w,h,fill,stroke):
  if x == None: x = 0
  if y == None: y = 0
  if h == None: h = 0
  if w == None: w = 0
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
  blueberry.color(stroke,fill)
  blueberry.penup()
  blueberry.pensize(1)
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

def line(x1,y1,x2,y2,size,stroke):
      if x1 == None: x1 = 0
      if y1 == None: y1 = 0
      if x2 == None: x2 = 0
      if y2 == None: y2 = 0
      if size == None: size = 1
      if stroke == None: stroke = "black"
      blueberry.color(stroke)
      blueberry.pensize(size)
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
    blueberry.pensize(1)
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
      if x == None: x = 0
      if y == None: y = 0
      if sides == None: sides = 3
      if size == None: size = 30
      if fill == None: fill = "black"
      if stroke == None: stroke = "black"
      blueberry.color(stroke,fill)
      blueberry.penup()
      blueberry.setx(x)
      blueberry.sety(y)
      blueberry.pendown()
      blueberry.pensize(1)
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

def loopgame():
      blueberry.mainloop()
      
def trace():
      blueberry.tracer(0,0)

def addimg(src):
      blueberry.addshape(src)

def shape(src):
      blueberry.shape(src)

def size(s):
      blueberry.pensize(s)
