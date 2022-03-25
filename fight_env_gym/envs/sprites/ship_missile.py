from typing import Tuple
from fight_env_gym.envs.sprites.base import Missile

import pygame


class ShipMissile(Missile):

    def __init__(self,
                 image: pygame.Surface,
                 screen_size: Tuple[int, int],
                 size: Tuple[int, int],
                 rect: Tuple[int, int],
                 speed: int = 10):
        super(ShipMissile, self).__init__(image, screen_size, size, rect, speed)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > self.screen_size[0]:
            self.kill()
