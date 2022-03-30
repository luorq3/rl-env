import math
from typing import Tuple

from fight_env_gym.envs.sprites.base import Missile

from pygame.rect import Rect


class FortMissile(Missile):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 radian: float,
                 speed: int = 1):
        super(FortMissile, self).__init__(screen_size, rect, speed)
        self.radian = radian
        self.distance = 0

    def update(self):
        self.distance += self.speed
        offset_x = self.distance * math.sin(self.radian)
        offset_y = self.distance * math.cos(self.radian)

        if 0 < self.rect.x - offset_x < self.max_rect[0] \
                and 0 < self.rect.y - offset_y < self.max_rect[1]:
            self.rect.x -= offset_x
            self.rect.y -= offset_y
        else:
            self.kill()
