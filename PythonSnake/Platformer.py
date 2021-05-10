import sys

import pygame

import physics

import map
import player as p

pygame.init()

tilesize = 64

world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
# World Gen
world = []
for row in range(len(world_data)):
    for col in range(len(world_data[row])):
        tile_id = world_data[row][col]
        if tile_id == 0:
            continue
        tile = map.Tile(tile_id, [col, row])
        world.append(tile)

clocks = pygame.time.Clock()
size = width, height = 1920, 1024
black = 0, 0, 0

can_jump = False

screen = pygame.display.set_mode(size)
ball = pygame.image.load("64x64.png")

player = p.Player()


v_input = pygame.Vector2()


def get_playerinput(event):

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w: v_input.y = v_input.y + 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w: v_input.y = v_input.y - 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: v_input.x = v_input.x - 1
        if event.type == pygame.KEYUP and event.key == pygame.K_a: v_input.x = v_input.x + 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s: v_input.y = v_input.y - 1
        if event.type == pygame.KEYUP and event.key == pygame.K_s: v_input.y = v_input.y + 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d: v_input.x = v_input.x + 1
        if event.type == pygame.KEYUP and event.key == pygame.K_d: v_input.x = v_input.x - 1
    return v_input


while 1:
    delta = clocks.tick()

    old_pos = pos.copy()

    player.move(v_input)
    # if keydownLeft:
    #     pos[0] = pos[0] - player.speed * delta
    # if keydownRight:
    #     pos[0] = pos[0] + player.speed * delta
    # if keydownUp:
    #     pos[1] = pos[1] - speed * delta
    # if keydownDown:
    #     pos[1] = pos[1] + speed * delta

    can_jump = player.is_grounded(world)
    player.update(world, get_playerinput())

    if pos[0] < 0:
        pos[0] = 0
    if pos[0] + player.get_rect().width > width:
        pos[0] = width - player.get_rect().width
    if pos[1] < 0:
        pos[1] = 0
    if pos[1] + player.get_rect().height > height:
        pos[1] = height - player.get_rect().height

    player.get_rect().update(pos, player.get_rect().size)

    for tile in world:
        if physics.has_collision(player.get_rect(), tile.get_rect()):
            if tile.get_id() == map.tile_type["ground"]:
                pos = old_pos
            if tile.get_id() == map.tile_type["kill"]:
                pos = [0, 0]
                print("died")

    player.get_rect().update(pos, player.get_rect().size)

    screen.fill(black)
    screen.blit(ball, player.get_rect())

    for tile in world:
        tile.draw(screen)

    pygame.display.flip()
