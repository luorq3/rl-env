from enum import IntEnum
from typing import Tuple

from fight_env_gym.envs.sprites import Ship
from fight_env_gym.envs.sprites import Fort
from fight_env_gym.envs.sprites import ShipMissile
from fight_env_gym.envs.sprites import FortMissile
from fight_env_gym.envs.utils import *


class GameLogic:

    def __init__(self, screen_size: Tuple[int, int]):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        images = load_images()
        self.ship = images['ship']
        self.fort = images['fort']

    def _create_sprite(self, sprite_class):
        # if sprite_class == 'ship':
        #     ship = Ship()
        pass

    class Action(IntEnum):
        NOOP, UP, DOWN, LEFT, RIGHT, FIRE = 0, 1, 2, 3, 4, 5

    def check_crash(self):
        pass

    def update_state(self, action: int):
        pass

