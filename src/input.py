#Created By Rabia Alhaffar In 13/January/2020
#Input For Blueberry
import turtle
import random
from turtle import *
from random import *
blueberry = turtle
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
    
