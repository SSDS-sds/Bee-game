import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Bee Game."

game_over = False
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

    if game_over:
        screen.fill("red")
        screen.draw.text("YOUR TIME IS OVER.", color = "white", fontsize = 50, midtop = (WIDTH/2,10))
        screen.draw.text(f"Your score is {score}", color = "white", fontsize = 35, midtop = (WIDTH/2,40))


def timer_is_up():
    global game_over
    game_over = True

def move_flower():
    flower.x = randint(50,550)
    flower.y = randint(50,450)

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2

    if bee.colliderect(flower):
        move_flower()
        score = score + 10

clock.schedule(timer_is_up, 60)




pgzrun.go()