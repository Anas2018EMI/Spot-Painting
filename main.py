import colorgram
from turtle import Turtle, Screen
import random

colors= colorgram.extract('spot_painting.jpg',200)

rgb_colors=[]
for color in colors:
    rgb_colors+=[(color.rgb.r, color.rgb.g, color.rgb.b)]

# rgb_colors=[(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
screen=Screen()
screen.colormode(255)

tim=Turtle()
tim.penup()
tim.setpos(-325,-290)

y=0

for _ in range(10):
    for _ in range(10):
       tim.dot(20, random.choice(rgb_colors))
       tim.forward(70)
    y+=1
    tim.setpos(-325,-290+70*y)

tim.setpos(0,0)















screen.exitonclick()