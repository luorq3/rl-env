import math
from typing import Tuple

import pygame

from fight_env_gym.envs.sprites.base import SpriteBase
from fight_env_gym.envs.sprites.fort_missile import FortMissile
from fight_env_gym.envs.utils import *

class Fort(SpriteBase):

    def __init__(self,
                 image: pygame.Surface,
                 screen_size: Tuple[int, int],
                 size: Tuple[int, int],
                 rect: Tuple[int, int],
                 hp: int = 3):
        super(Fort, self).__init__(image, screen_size, size, rect)
        self.hp = hp
        # self.angle = 0
        self.radian = 0
        self.missile_group = pygame.sprite.Group()

    def fire(self):
        missile = FortMissile(
            load_image("fort_missile"),
            self.screen_size, (10, 10),
            (self.rect.x, self.rect.y),
            self.radian)
        self.missile_group.add(missile)

    def update(self, target_x, target_y, *args: Any, **kwargs: Any) -> None:
        offset_x = self.rect.x - target_x
        offset_y = self.rect.y - target_y
        self.radian = math.atan(offset_y / offset_x)
        # self.angle = self.radian * 180 / math.pi

