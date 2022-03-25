from typing import Tuple

from fight_env_gym.envs.sprites.base import Shell

import pygame


IMAGE_PATH = '../assets/fort_bullet.png'

class FortShell(Shell):

    def __init__(self,
                 bg_size: Tuple[int, int],
                 rect: Tuple[int, int],
                 size: Tuple[int, int] = (20, 20),
                 speed: int = 10):
        self.image = pygame.image.load(IMAGE_PATH)
        super(FortShell, self).__init__(bg_size, self.image, rect, size, speed)

    def launch(self):
        pass

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.kill()
