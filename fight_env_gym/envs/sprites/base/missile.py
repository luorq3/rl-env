from typing import Tuple, Any

import pygame
from fight_env_gym.envs.sprites.base import SpriteBase


class Missile(SpriteBase):

    def __init__(self,
                 image: pygame.Surface,
                 bg_size: Tuple[int, int],
                 size: Tuple[int, int],
                 rect: Tuple[int, int],
                 speed: int = 10):
        super(Missile, self).__init__(image, bg_size, size, rect)
        self.speed = speed

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass
