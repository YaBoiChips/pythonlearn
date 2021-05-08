import sys

import pygame

pygame.init()

clocks = pygame.time.Clock()
size = width, height = 1000, 1000
speed = 1
black = 0, 0, 0
pos = [0.0, 0.0]


keydownUp = False
keydownDown = False
keydownLeft = False
keydownRight = False

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Screenshot 2021-05-03 185911.png")
ballrect = ball.get_rect()

while 1:
    delta = clocks.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w: keydownUp = True
        if event.type == pygame.KEYUP and event.key == pygame.K_w: keydownUp = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: keydownLeft = True
        if event.type == pygame.KEYUP and event.key == pygame.K_a: keydownLeft = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s: keydownDown = True
        if event.type == pygame.KEYUP and event.key == pygame.K_s: keydownDown = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d: keydownRight = True
        if event.type == pygame.KEYUP and event.key == pygame.K_d: keydownRight = False

    if keydownDown:
        pos[1] = pos[1] + speed * delta
    #if ballrect.left < 0:
        #speed[0] = -speed[0]
        #pos[0] = 0
    #if ballrect.right > width:
        #speed[0] = -speed[0]
        #pos[0] = width - ballrect.width
    #if ballrect.top < 0:
        #speed[1] = -speed[1]
        #pos[1] = 0
    #if ballrect.bottom > height:
        #speed[1] = -speed[1]
        #pos[1] = height - ballrect.height
    ballrect.update(pos, ballrect.size)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
