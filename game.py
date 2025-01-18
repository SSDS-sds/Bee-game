import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Bee Game."

score = 0

bee = Actor("bee")
bee.pos = 300,250
flower = Actor("flower")
flower.pos = 400,350

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+ str(score), color = "red", fontsize = 30, topleft = (10,10))

pgzrun.go()