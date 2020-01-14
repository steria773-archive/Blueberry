#Created By Rabia Alhaffar In 13/January/2020
#Input For Blueberry
import turtle
import random
from turtle import *
from random import *
blueberry = turtle
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
