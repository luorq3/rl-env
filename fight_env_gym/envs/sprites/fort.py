import math
from typing import Tuple

import pygame

from fight_env_gym.envs.sprites.base import SpriteBase
from fight_env_gym.envs.sprites.fort_missile import FortMissile
from fight_env_gym.envs.utils import *


class Fort(SpriteBase):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 hp: int = 3):
        super(Fort, self).__init__(screen_size, rect)
        self.hp = hp
        # self.angle = 0
        self.radian = math.pi / 2
        self.fort_group = pygame.sprite.Group()

    def fire(self):
        missile = FortMissile(
            self.screen_size,
            self.rect.copy(),
            self.radian)
        self.fort_group.add(missile)

    def update(self, target_x, target_y, *args: Any, **kwargs: Any) -> None:
        offset_x = self.rect.x - target_x
        offset_y = self.rect.y - target_y
        if offset_y != 0:
            self.radian = math.atan(offset_x / offset_y)
        else:
            self.radian = math.pi / 2
        # self.angle = self.radian * 180 / math.pi

