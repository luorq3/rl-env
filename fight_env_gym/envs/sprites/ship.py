from typing import Tuple
from fight_env_gym.envs.sprites.base import SpriteBase, Movable
from fight_env_gym.envs.sprites.ship_missile import ShipMissile
from fight_env_gym.envs.utils import *

import pygame


class Ship(SpriteBase, Movable):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 speed: int = 10,
                 hp: int = 3):
        SpriteBase.__init__(self, screen_size, rect)
        Movable.__init__(self, self, speed)
        self.hp = hp
        self.missile_group = pygame.sprite.Group()

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass

    def fire(self):
        missile = ShipMissile(self.screen_size, self.rect.copy())
        self.missile_group.add(missile)


# s = Ship(pygame.surface.Surface((10, 10)), (50, 50), (10, 10), (0, 0))
