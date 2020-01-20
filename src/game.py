#Created By Rabia Alhaffar In 13/January/2020
#For Controlling Game And It's Window
import turtle,random
from turtle import *
from random import *
blueberry = turtle
def closegame():
    blueberry.bye()

def resize(h,w):
      if h == None: h = 600
      if w == None: w = 600
      bwindow = Screen()  
      bwindow.setup(width=w , height=h ) 
      blueberry = turtle
      windowheight = blueberry.window_height()
      windowwidth = blueberry.window_width()
      bturtle = blueberry.Turtle()
      blueberry.speed(0) 
      blueberry.hideturtle()
