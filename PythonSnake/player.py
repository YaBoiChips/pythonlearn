import pygame
from pygame.math import Vector2

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
        y_overlap = False
        for tile in world:
            if tile.get_id() == map.tile_type["ground"]:
                y_overlap = (self._rect.bottom ==
                             tile.get_rect().top) or y_overlap
        return y_overlap

    def get_rect(self):
        return self._rect

    def update(self, delta, world, player_input):
        self._physics_object.velocity.x = player_input.x * self.speed * delta

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
