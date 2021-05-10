import pygame

tilesize = 64
tile_type = {
    "ground": 1,
    "kill": 2
}


class Tile:
    _rect = None
    _id = -1
    _pos = [0, 0]

    def __init__(self, t_id, pos):
        self._rect = pygame.Rect(pos[0] * tilesize, pos[1] * tilesize, tilesize, tilesize)
        self._id = t_id
        self._pos = pos

    def get_rect(self):
        return self._rect

    def get_id(self):
        return self._id

    def draw(self, screen):
        if self._id == tile_type["ground"]:
            pygame.draw.rect(screen, (255, 255, 255), self._rect)
        elif self._id == tile_type["kill"]:
            pygame.draw.rect(screen, (255, 0, 0), self._rect)
