import pygame
from pygame.math import Vector2

import map


class Player:
    _rect = None
    _pos = Vector2()
    speed = 0.5
    _image = pygame.image.load("64x64.png")

    def __init__(self):
        self._rect = self._image.get_rect()

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
        self._pos.x = self._pos.x + player_input.x * self.speed
        self._rect.update(self._pos, self._rect.size)

    def draw(self, screen):
        screen.blit(self._image, self._rect)

    # def move(self, v_input):
    #     pass
