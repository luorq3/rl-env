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
                 speed: int = 10,
                 hp: int = 3):
        super(Fort, self).__init__(image, screen_size, size, rect)
        self.hp = hp

    def fire(self, fort_shell_sprites, all_sprites):
        shell = FortMissile(load_image("fort_missile"), self.screen_size, (10, 10), (self.rect.x, self.rect.y))

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass
