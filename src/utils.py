#Created By Rabia Alhaffar In 14/January/2020
#Utilities For Blueberry Game Programming Library,It Uses Python

import random,turtle,math,webbrowser
from random import *
from turtle import *
from math import *
from webbrowser import *

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
blueberry = turtle

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