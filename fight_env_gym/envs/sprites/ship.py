from typing import Tuple
from fight_env_gym.envs.sprites.base import SpriteBase, Movable
from fight_env_gym.envs.sprites import ShipMissile
from fight_env_gym.envs.utils import *

import pygame


class Ship(SpriteBase, Movable):

    def __init__(self,
                 image: pygame.Surface,
                 screen_size: Tuple[int, int],
                 size: Tuple[int, int],
                 rect: Tuple[int, int],
                 speed: int = 10,
                 hp: int = 3):
        SpriteBase.__init__(self, image, screen_size, size, rect)
        Movable.__init__(self, self, speed)
        self.hp = hp

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass

    def fire(self):
        shell = ShipMissile(load_image("ship_missile"), self.screen_size, (10, 10), (self.rect.x, self.rect.y))


# s = Ship(pygame.surface.Surface((50, 50)), (100, 100), (10, 10), (0, 0))
