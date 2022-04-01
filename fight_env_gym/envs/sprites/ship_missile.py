from typing import Tuple
from fight_env_gym.envs.sprites.base import Missile

from pygame.rect import Rect


class ShipMissile(Missile):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 speed: int = 10):
        super(ShipMissile, self).__init__(screen_size, rect, speed)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
