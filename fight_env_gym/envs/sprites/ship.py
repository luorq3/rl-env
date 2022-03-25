from typing import Tuple
from pygame.locals import *
from fight_env_gym.envs.sprites.base import Movable
from fight_env_gym.envs.sprites.ship_shell import ShipShell

import pygame


IMAGE_PATH = '../assets/ship.png'

class Ship(Movable):
    def __init__(self,
                 bg_size: Tuple[int, int],
                 rect: Tuple[int, int],
                 size: Tuple[int, int] = (20, 20),
                 speed: int = 10):
        self.image = pygame.image.load(IMAGE_PATH)
        super(Ship, self).__init__(bg_size, self.image, rect, size, speed)
        self.defense = 3

    def handle(self, key_pressed, ship_shell_sprites, all_sprites):
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.move_right()
        self.launch(key_pressed, ship_shell_sprites, all_sprites)

    def launch(self, key_pressed, ship_shell_sprites, all_sprites):
        if key_pressed[K_SPACE]:
            shell = ShipShell(self.bg_size, (self.rect.x, self.rect.y))
            ship_shell_sprites.add(shell)
            all_sprites.add(shell)
