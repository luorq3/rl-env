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
                 hp: int = 5):
        super(Fort, self).__init__(screen_size, rect)
        self.hp = hp
        self.angle = 0
        self.radian = math.pi / 2
        self.missile_group = pygame.sprite.Group()

    def fire(self):
        missile = FortMissile(
            self.screen_size,
            self.rect.copy(),
            self.radian)
        self.missile_group.add(missile)

    def update(self, target_x, target_y, *args: Any, **kwargs: Any) -> None:
        offset_x = self.rect.x - target_x
        offset_y = self.rect.y - target_y

        # x_is_pos = offset_x > 0
        # y_is_pos = offset_y > 0
        #
        # if offset_y == 0:
        #     if x_is_pos:
        #         self.radian = math.pi / 2
        #     else:
        #         self.radian = - math.pi / 2
        #
        #     return
        #
        # self.radian = math.atan(math.fabs(offset_x / offset_y))
        #
        # if y_is_pos:
        #     if x_is_pos:
        #         return

        if offset_y != 0:
            self.radian = math.atan(offset_x / offset_y)
        else:
            self.radian = math.pi / 2
        self.angle = self.radian * 180 / math.pi
        # if self.radian < 0:
        #     self.radian += math.pi

