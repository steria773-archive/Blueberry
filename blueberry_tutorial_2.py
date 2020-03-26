import blueberry
from blueberry import *

#Creates A Game Window 
#With Title And Size Of 600x600 
init(600,600,"Graphics Master!!!")

#Shapes And Text
text(-100,-200,"Hello World",False,"center","arial",16,"bold")
rect(100,-50,50,50,"blue","black")
circle(50,-50,50,"red","black")
square(0,-50,50,"green","black")
polysides(200,100,6,60,"purple","black")
poly([[100,100],[50,50],[200,100],[100,100]],"orange","black")
line(100,100,-100,-100,10,"black")

#Wait For User Input(In Python Console)
input()