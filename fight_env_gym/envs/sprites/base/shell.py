from abc import ABC
from typing import Tuple
from fight_env_gym.envs.sprites.base import Movable

import pygame


class Shell(Movable, ABC):

    def __init__(self,
                 bg_size: Tuple[int, int],
                 sprite: pygame.surface.Surface,
                 rect: Tuple[int, int],
                 size: Tuple[int, int],
                 speed: int = 10):
        super(Shell, self).__init__(bg_size, sprite, rect, size, speed)

    def launch(self):
        raise NotImplementedError
