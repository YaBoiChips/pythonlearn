import pygame
from pygame.math import Vector2
import math

import map
from physics import PhysicsObject

GRAVITY = 0.003

class Player:
    _rect = None
    _image = pygame.image.load("64x64.png")
    _physics_object = None
    
    speed = 0.5

    def __init__(self):
        self._rect = self._image.get_rect()
        self._physics_object = PhysicsObject(self)

    def is_grounded(self, world):
        # y_overlap = False
        # for tile in world:
        #     if tile.get_type() == "ground":
        #         y_overlap = (self._rect.bottom ==
        #                      tile.get_rect().top) or y_overlap
        # return y_overlap

        # get the tiles below the player sprite
        l = self._rect.left / map.TILE_SIZE
        r = self._rect.right / map.TILE_SIZE
        b = self._rect.bottom / map.TILE_SIZE

        tiles = []
        tiles.append(map.get_tile_type(math.floor(l), math.floor(b)))
        tiles.append(map.get_tile_type(math.floor(r), math.floor(b)))

        for tile in tiles:
            if tile == "ground" and self._physics_object.velocity.y == 0:
                return True

        return False




    def get_rect(self):
        return self._rect

    def update(self, delta, world, player_input):
        self._physics_object.velocity.x = player_input.x * self.speed * delta

        if player_input.y > 0 and self.is_grounded(world):
            self._physics_object.add_force(Vector2(0, -0.5))

        # apply forces
        self._physics_object.add_force(Vector2(0, GRAVITY))
        # compute physics
        self._physics_object.update(delta, world)

        # update pygame objects
        self._rect.update(self._physics_object.position, self._rect.size)

    def draw(self, screen):
        screen.blit(self._image, self._rect)

    # def move(self, v_input):
    #     pass
