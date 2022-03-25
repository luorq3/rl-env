from typing import Tuple

import pygame


class Movable(pygame.sprite.Sprite):

    def __init__(self,
                 bg_size: Tuple[int, int],
                 sprite: pygame.surface.Surface,
                 rect: Tuple[int, int],
                 size: Tuple[int, int],
                 speed: int):
        super(Movable, self).__init__()
        self.bg_size = bg_size
        self.rect = sprite.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.size = size
        self.speed = speed
        self.max_rect = [rect - size for size, rect in zip(self.size, self.bg_size)]

    def move_up(self):
        if self.rect.y > self.speed:
            self.rect.y -= self.speed
        else:
            self.rect.y = 0

    def move_down(self):
        if self.rect.y < self.max_rect[1]:
            self.rect.y += self.speed
        else:
            self.rect.y = self.max_rect[1]

    def move_left(self):
        if self.rect.x > self.speed:
            self.rect.x -= self.speed
        else:
            self.rect.x = 0

    def move_right(self):
        if self.rect.x < self.max_rect[0]:
            self.rect.x += self.speed
        else:
            self.rect.x = self.max_rect[0]
