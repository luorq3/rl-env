from enum import IntEnum
from typing import Tuple

from fight_env_gym.envs.sprites import Ship
from fight_env_gym.envs.sprites import Fort
from fight_env_gym.envs.utils import *


ship_size = (40, 99)
fort_size = (20, 20)

class GameLogic:

    def __init__(self, images, screen_size: Tuple[int, int]):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        self.ship = Ship(screen_size, Rect(*self._ship_init_position(), *ship_size))
        self.fort = Fort(screen_size, Rect(*self._fort_init_position(), *fort_size))

        self.fort_fire_speed = 30  # TODO: The value is inversely proportional to the fire_speed, to be perfected
        self.fort_fire_clock = 0

        # hit mask
        # self.ship_mask = get_hitmask(images["ship"])
        # self.fort_mask = get_hitmask(images["fort"])
        # self.ship_missile_mask = images["ship_missile"]
        # self.fort_missile_mask = images["fort_missile"]

    class Action(IntEnum):
        NOOP, UP, DOWN, LEFT, RIGHT, FIRE = 0, 1, 2, 3, 4, 5

    class Reward(IntEnum):
        FIRE, HIT, BE_HIT, DESTROY, BE_DESTROY, VICTORY, DEFEATED = -1, 2, -2, 3, -3, 4, -4

    def _ship_init_position(self, nums=1):
        if nums == 1:
            return self._screen_width // 2, self._screen_height
        else:
            # TODO: multi ship position initialization
            return 0, 0

    def _fort_init_position(self, nums=1):
        if nums == 1:
            return self._screen_width // 2, 0
        else:
            # TODO: multi ship position initialization
            return 0, 0

    def update_state(self, action: int):
        alive = True
        reward = 0

        if action in [1, 2, 3, 4]:
            self.ship.move(action)
        if action == 5:
            reward += self.Reward.FIRE
            self.ship.fire()

        # machine fort fire logic
        if self.fort_fire_clock % self.fort_fire_speed == 0:
            self.fort.update(*self.ship.rect[:2])
            self.fort.fire()
            self.fort_fire_clock = 0

        self.fort_fire_clock += 1

        # Collision check
        # Was Fort be hit
        for missile in self.ship.missile_group:
            # collided = pixel_collision(self.fort.rect, missile.rect, self.fort_mask, self.ship_missile_mask)
            collided = pixel_collision2(self.fort.rect, missile.rect)
            if collided:
                missile.kill()
                self.fort.hp -= 1
                reward += self.Reward.HIT
            if self.fort.hp == 0:
                alive = False
                reward += self.Reward.VICTORY
        # Was Ship be hit
        for missile in self.fort.missile_group:
            # collided = pixel_collision(self.ship.rect, missile.rect, self.ship_mask, self.fort_missile_mask)
            collided = pixel_collision2(self.ship.rect, missile.rect)
            if collided:
                missile.kill()
                self.ship.hp -= 1
                reward += self.Reward.BE_HIT
            if self.ship.hp == 0:
                alive = False
                reward += self.Reward.DEFEATED

        return reward, alive

