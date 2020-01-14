#Created By Rabia Alhaffar In 13/January/2020
#Blueberry Game Library For Python
#NOTES: It Uses turtle Module So It Requires Python 2.5+

#Modules
import turtle,random,math,sys,os,webbrowser,platform,playsound
from turtle import *
from random import *
from math import *
from os import *
from webbrowser import *
from platform import *
from sys import *
from playsound import *

#Variables
blueberry = turtle
os_name = os.name
os_release = release()
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
disposed = 0

#Graphics Functions
#Created By Rabia Alhaffar In 13/January/2020
#Graphics Module For Blueberry,In Development!!!
#NOTES: It Uses turtle Module So It Requires Python 2.5+
import turtle,random
from turtle import *
from random import *

blueberry = turtle

def init(h,w,t):
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
  bscreen.update()

def beginfill():
  blueberry.begin_fill()

def endfill():
  blueberry.end_fill()

def focus():
  blueberry.listen()

def triangle(x,y,a,b,c,fill,stroke):
  if x == None: x = 0
  if y == None: y = 0
  if a == None: a = 0
  if b == None: b = 0
  if c == None: c = 0
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
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
  if x == None: x = 0
  if y == None: y = 0
  if h == None: h = 0
  if w == None: w = 0
  if fill == None: fill = "black"
  if stroke == None: stroke = "black"
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

def size(s):
      blueberry.pensize(s)

#Input Functions
def exitclick():
    blueberry.exitonclick()
    
def bindkey(k,f):
    blueberry.onkey(f,k)
    
def presskey(k,f):
    blueberry.onkeypress(f,k)

def releasekey(k,f):
    blueberry.onkeyrelease(f,k)

def click(f):
    blueberry.onclick(f)
  
#CMD Functions
def execute(commands):
  os.system(commands)
  
def process(loc):
  os.system("start " + loc)
  
#Game Misc Functions
def closegame():
    blueberry.bye()

def resize(h,w):
    if h == None: h = 600
    if w == None: w = 600
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
#To Swap Between Colors,Can Be For Values
def swapvalues(a,b):
    if a == None: a = 0
    if b == None: b = 0
    disposed = a
    a = b
    b = disposed

#Random Value Getted Between num1 And num2
def randbetween(num1,num2):
    if num1 == None: num1 = 0
    if num2 == None: num2 = 2
    return randrange(num1,num2)

#Random Value Generated Between 0 And num
def rand(num):
    if num == None: num = 1
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

def openurl(url):
    webbrowser.open_new(url)