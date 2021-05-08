import sys

import pygame

pygame.init()

tilesize = 64

world_data = [
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
]

world = []
for row in range(len(world_data)):
    for col in range(len(world_data[row])):
        tile_id = world_data[row][col]
        if tile_id == 0:
            continue
        if tile_id == 1:
            tile = pygame.Rect(col * tilesize, row * tilesize, tilesize, tilesize)
            world.append(tile)


clocks = pygame.time.Clock()
size = width, height = 1600, 1000
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
    if keydownUp:
        pos[1] = pos[1] - speed * delta
    if keydownLeft:
        pos[0] = pos[0] - speed * delta
    if keydownRight:
        pos[0] = pos[0] + speed * delta

    if pos[0] < 0:
        pos[0] = 0
    if pos[0] + ballrect.width > width:
        pos[0] = width - ballrect.width
    if pos[1] < 0:
        pos[1] = 0
    if pos[1] + ballrect.height > height:
        pos[1] = height - ballrect.height

    ballrect.update(pos, ballrect.size)

    screen.fill(black)
    screen.blit(ball, ballrect)
    for tile in world:
        pygame.draw.rect(screen, (255, 255, 255), tile)
    pygame.display.flip()
