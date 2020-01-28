#Created By Rabia Alhaffar In 13/January/2020
#Physics Part For Blueberry
#NOTES: It Is Rewritten From JavaScript Game Framework Called Cake
#https://github.com/Rabios/Cake
import turtle
import random
import math
from turtle import *
from random import *
from math import *
blueberry = turtle
def collisionrects(r1_x,r1_y,r1_w,r1_h,r2_x,r2_y,r2_w,r2_h):
    if r1_x < r2_x + r2_w and r1_x + r1_w > r2_x and r1_y < r2_y + r2_h and r1_y + r1_h > r2_y:
        return True
    else: return False

def collisioncircles(c1_x,c1_y,c1_r,c2_x,c2_y,c2_r):
    dx = c1_x - c2_x
    dy = c1_y + c2_y
    dist = math.sqrt(dx * dx + dy * dy)
    if dist < c1_r + c2_r: return True
    else: return False

def collisioncirclerect(c1_x,c1_y,c1_r,r1_x,r1_y,r1_w,r1_h):
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
