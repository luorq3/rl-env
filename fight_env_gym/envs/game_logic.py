from enum import IntEnum
from typing import Tuple

from fight_env_gym.envs.sprites import Ship
from fight_env_gym.envs.sprites import Fort
from fight_env_gym.envs.utils import *


class GameLogic:

    def __init__(self, screen_size: Tuple[int, int]):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        self.ship = Ship(screen_size, Rect(0, 0, 10, 10))
        self.fort = Fort(screen_size, Rect(500, 400, 10, 10))

    class Action(IntEnum):
        NOOP, UP, DOWN, LEFT, RIGHT, FIRE = 0, 1, 2, 3, 4, 5

    def check_crash(self):
        pass

    def update_state(self, action: int):
        if action in [1, 2, 3, 4]:
            self.ship.move(action)
        if action == 5:
            self.ship.fire()

        self.fort.fire()

        return True

