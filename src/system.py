# Written By Rabia Alhaffar In 12/January/2020
import os,platform,sys,system
from os import *
from platform import *
from sys import *
from system import *
os_name = os.name
os_release = release()
def execute(commands):
  os.system(commands)

def process(loc):
  os.system("start " + loc)