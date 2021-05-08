import sys

import pygame

import physics

pygame.init()

tilesize = 64

world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
size = width, height = 1920, 960
speed = 0.5
black = 0, 0, 0
pos = [0.0, 0.0]

keydownUp = False
keydownDown = False
keydownLeft = False
keydownRight = False

screen = pygame.display.set_mode(size)

ball = pygame.image.load("64x64.png")
playerrect = ball.get_rect()

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

    old_pos = pos.copy()
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
    if pos[0] + playerrect.width > width:
        pos[0] = width - playerrect.width
    if pos[1] < 0:
        pos[1] = 0
    if pos[1] + playerrect.height > height:
        pos[1] = height - playerrect.height

    playerrect.update(pos, playerrect.size)

    for tile in world:
        if physics.has_collision(playerrect, tile):
            pos = old_pos

    playerrect.update(pos, playerrect.size)

    screen.fill(black)
    screen.blit(ball, playerrect)
    for tile in world:
        pygame.draw.rect(screen, (255, 255, 255), tile)
    pygame.display.flip()
