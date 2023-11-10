import random

import pygame.font
from random import *
from pygame import *
init()

win_width = 700
win_height = 500
FPS = 60
clock = time.Clock()
window = display.set_mode((win_width, win_height))
yspeed = 4

bg = "board.jpg"
back = transform.scale(image.load(bg), (win_width, win_height))


run = True

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, img, x, y, w, h, speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ballr = GameSprite("png-transparent-bitter-orange-peel-town-information-ping-pong-ball-sport-orange-sphere-thumbnail-removebg-preview.png",335,235,30,30, 4)
p1 = GameSprite("racket.png", 10, 200, 10, 60, 6)
p2 = GameSprite("racket.png", 680, 200, 10, 60, 6)
p3 = GameSprite("Untitled design.jpg", 320, 10, 60, 10, 6)
p4 = GameSprite("Untitled design.jpg", 320, 480, 60, 10, 6)
team1score = 0
team2score = 0
font = pygame.font.SysFont("Comic Sans MS", 60)
game = True


while run:

    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            run = False
    if game:
        if team1score ==15:

            game = not game
        if team2score == 15:

            game = not game
        window.blit(back, (0, 0))
        p1txt = font.render(str(team1score), True, (250, 250, 250))
        p2txt = font.render(str(team2score), True, (0, 0, 0))
        window.blit(p1txt, (260, 210))
        window.blit(p2txt, (332.5, 150))
        window.blit(p1txt, (400, 210))
        window.blit(p2txt, (332.5, 270))
        ballr.reset()
        p1.reset()
        p2.reset()
        p3.reset()
        p4.reset()
        if keys[K_s] and p1.rect.y<=430:
            p1.rect.y+=p1.speed
        if keys[K_w] and p1.rect.y>=10:
            p1.rect.y -= p1.speed
        if keys[K_UP] and p2.rect.y>=10:
            p2.rect.y -= p2.speed
        if keys[K_DOWN] and p2.rect.y<=430:
            p2.rect.y += p2.speed
        if keys[K_y]:
            p3.rect.x-= p3.speed
        if keys[K_u]:
            p3.rect.x += p3.speed
        if keys[K_n]:
            p4.rect.x -= p4.speed
        if keys[K_m]:
            p4.rect.x += p4.speed
        if ballr.rect.y>=470:
            yspeed*=-1
            team1score+=1
        if ballr.rect.x>=670:
            ballr.speed*=-1
            team2score+=1
        if ballr.rect.y <= 0:
            yspeed *= -1
            team1score+=1
        if ballr.rect.x <= 0:
            ballr.speed *= -1
            team2score+=1

        if ballr.rect.colliderect(p1):
            ballr.speed *= -1.09
            p1.speed *= 1.03
            sound = mixer.Sound("funny-spring-jump-140378.mp3")
            sound.play()
        if ballr.rect.colliderect(p2):
            ballr.speed *= -1.09
            p2.speed *= 1.03
            sound = mixer.Sound("funny-spring-jump-140378.mp3")
            sound.play()
        if ballr.rect.colliderect(p3):
            yspeed *= -1.09
            p3.speed *= 1.03
            sound = mixer.Sound("funny-spring-jump-140378.mp3")
            sound.play()
        if ballr.rect.colliderect(p4):
            yspeed *= -1.09
            p4.speed *= 1.03
            sound = mixer.Sound("funny-spring-jump-140378.mp3")
            sound.play()

        ballr.rect.x += ballr.speed

        ballr.rect.y += yspeed
    if keys[K_r] and game == False:
        ballr.rect.x, ballr.rect.y = 335, 225
        p1.rect.y, p2.rect.y = 200,200
        ballr.speed = 4/1.3
        yspeed = 4/1.3
        p1.speed, p2.speed,p3.speed, p4.speed = 6, 6, 6, 6
        team1score = 0
        team2score = 0
        game = not game
    display.update()
    clock.tick(FPS)