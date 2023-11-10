import random

import pygame.font
from random import *
from pygame import *
init()
mixer.music.load("girl-a-siinamota.mp3")
mixer.music.play(-1)
win_width = 700
win_height = 500
FPS = 60
clock = time.Clock()
window = display.set_mode((win_width, win_height))
yspeed = 4

bg = "Untitled design.png"
back = transform.scale(image.load(bg), (win_width, win_height))


run = True

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, img, x, y, w, h, speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен збeрігати властивість image - зображення
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ballr = GameSprite("png-transparent-bitter-orange-peel-town-information-ping-pong-ball-sport-orange-sphere-thumbnail-removebg-preview.png",335,235,30,30, 4)
p1 = GameSprite("racket.png", 0, 0, 200, 500, 6)
p2 = GameSprite("racket.png", 500, 0, 200, 500, 6)
p1losescore = 0
p2losescore = 0
font = pygame.font.SysFont("Comic Sans MS", 60)
game = True
p1count = 0
p2count = 0
while run:

    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            run = False
    if game:
        window.blit(back, (0, 0))
        if p1losescore>=30:
            window.blit(win,(250,200))
            game = not game
        if p1losescore <= -30:
            window.blit(lose, (250, 200))
            game = not game




        p1txt = font.render(str(p1losescore), True, (250, 250, 250))
        win = font.render("YOU WIN", True, (250, 250, 250))
        lose = font.render("YOU LOSE", True, (250, 250, 250))
        window.blit(p1txt, (230, 100))
        p1.reset()
        p2.reset()
        ballr.reset()

        if ballr.rect.y>=470:
            yspeed*=-1
        if ballr.rect.x>=670:
            ballr.speed*=-1

        if ballr.rect.y <= 0:
            yspeed *= -1
        if ballr.rect.x <= 0:
            ballr.speed *= -1
            p1losescore-=1
        if not keys[K_SPACE] and p1count>0:
            p1count-=1

        if keys[K_SPACE]:
            p1count+=0.1


        if ballr.rect.colliderect(p1) and keys[K_SPACE] and ballr.speed<0 and p1count<1.1:
            p1losescore+=1
            ballr.speed*=-1
            if ballr.speed<=3:
                ballr.speed *= 1.04
            p1.speed *= 1.03


        if ballr.rect.colliderect(p2) and ballr.speed>0:
            ballr.speed*=-1
            if ballr.speed <= 5:
                ballr.speed *= 1.04
            p2.speed *= 1.03



        ballr.rect.x += ballr.speed

        ballr.rect.y += yspeed
    if keys[K_r] and game == False:
        ballr.rect.x, ballr.rect.y = 335, 225
        p1.rect.y, p2.rect.y = 0,0
        ballr.speed = 4/1.3
        yspeed = 4/1.3
        p1.speed, p2.speed = 6, 6
        p1losescore = 0
        p2losescore = 0
        game = not game
    display.update()
    clock.tick(FPS)