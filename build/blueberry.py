#Created By Rabia Alhaffar In 13/January/2020
#Blueberry Game Library For Python
#NOTES: It Uses turtle Module So It Requires Python 2.5+

#Modules
import turtle,random,math,sys,os,platform,playsound
from turtle import *
from random import *
from math import *
from os import *
from platform import *
from sys import *
from playsound import *

#Variables
blueberry = turtle
os_name = os.name
os_release = release()

#Graphics Functions
#Created By Rabia Alhaffar In 13/January/2020
#Graphics Module For Blueberry,In Development!!!
#NOTES: It Uses turtle Module So It Requires Python 2.5+
import turtle,random
from turtle import *
from random import *

blueberry = turtle

def init(h,w,t):
      bwindow = Screen()  
      bwindow.setup(width=w , height=h ) 
      blueberry = turtle
      windowheight = blueberry.window_height()
      windowwidth = blueberry.window_width()
      bturtle = bluberry.Turtle()
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
  bscreen.update()

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

def loopgame():
      bscreen.mainloop()
      
def trace():
      bscreen.tracer(0,0)

def addimg(src):
      bscreen.addshape(src)

def shape(src):
      bscreen.shape(src)

#Input Functions
def exitclick():
    blueberry.exitonclick()
    
def bindkey(f,k):
    blueberry.onkey(f,k)
    
def presskey(f,k):
    blueberry.onkeypress(f,k)

def releasekey(f,k):
    blueberry.onkeyrelease(f,k)

def click(f):
    blueberry.onclick(f)
  
#CMD Functions
def execute(commands):
  os.system(commands)
  
#Game Misc Functions
def closegame():
    blueberry.bye()

def resize(h,w):
    blueberry.screensize(w,h)
    
#GUI Functions
def textinput(title,prompt):
    blueberry.textinput(title,prompt)

def numinput(title,prompt):
    blueberry.numinput(title,prompt)
    
#Physics Functions
def collisionrects(r1_x,r1_y,r1_h,r1_w,r2_x,r2_y,r2_h,r2_w):
    if r1_x < r2_x + r2_w and r1_x + r1_w > r2_x and r1_y < r2_y + r2_h and r1_y + r1_h > r2_y:
        return True
    else: return False

def collisioncircles(c1_x,c1_y,c1_r,c2_x,c2_y,c2_r):
    dx = c1_x - c2_x
    dy = c1_y + c2_y
    dist = math.sqrt(dx * dx + dy * dy)
    if dist < c1_r + c2_r: return True
    else: return False

def collisioncirclerect(c1_x,c1_y,c1_r,r1_x,r1_y,r1_h,r1_w):
    distx = abs(c1_x - r1_x - r1_w / 2)
    disty = abs(c1_y - r1_y - r1_h / 2)
    if distx <= (r1_w / 2): return True
    if disty <= (r1_h / 2): return True
    if distx > (r1_w / 2 + c1_r): return False
    if disty > (r1_h / 2 + c1_r): return False
    dx = distx - r1_w / 2
    dy = disty - r1_h / 2

def collisionwindowleft(ox,ow):
    if ox <= ow * 0.5: return True
    else: return False

def collisionwindowright(ox,ow):
    if ox + ow >= blueberry.window_width() + ow * 0.5: return True
    else: return False

def collisionwindowtop(oy,oh):
    if oy <= oh * 0.5: return True
    else: return False

def collisionwindowbottom(oy,oh):
    if oy + oh >= blueberry.window_height() + oh * 0.5: return True
    else: return False

#Audio
from playsound import *
def playaudio(src):
  playsound(src)

#Utilities
#Colors
red = "red"
orange = "orange"
yellow = "yellow" 
green = "green"
blue = "blue"
pink = "pink"
purple = "purple"
silver = "silver"
white = "white"
cyan = "cyan"
black = "black"
aqua = "aqua"
grey = "grey"

#Utilities Use
disposed = 0

#To Swap Between Colors,Can Be For Values
def swapvalues(a,b):
    disposed = a
    a = b
    b = disposed

#Random Value Getted Between num1 And num2
def randbetween(num1,num2):
    return randrange(num1,num2)

#Random Value Generated Between 0 And num
def rand(num):
    return math.floor(math.random() * num)

#Random Fill And Stroke Color
def randcolor():
    blueberry.color((randrange(0,256),randrange(0,256),randrange(0,256)),(randrange(0,256),randrange(0,256),randrange(0,256)))

#Random Fill Color
def randfill():
    blueberry.fillcolor((randrange(0,256),randrange(0,256),randrange(0,256)))

#Random Stroke Color
def randstroke():
    blueberry.pencolor((randrange(0,256),randrange(0,256),randrange(0,256)))
