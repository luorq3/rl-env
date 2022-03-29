from typing import Tuple

import pygame
from fight_env_gym.envs.utils import *

# Sea blue
FILL_BACKGROUND_COLOR = (135, 206, 235)

class FightRenderer:

    def __init__(self, screen_size: Tuple[int, int] = (700, 512)):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        self.display = None
        self.surface = pygame.Surface(screen_size)

        self.images = load_images(convert=False)

        self.game = None
        self._clock = pygame.time.Clock()

    def make_display(self) -> None:
        self.display = pygame.display.set_mode((self._screen_width, self._screen_height))
        for name, value in self.images.items():
            if value is None:
                continue

            if type(value) in (tuple, list):
                self.images[name] = tuple([img.convert_alpha() for img in value])
            else:
                self.images[name] = (value.convert() if name == "background" else value.convert_alpha())

    def draw_surface(self) -> None:
        if self.game is None:
            raise ValueError("A game logic must be assigned to the renderer!")

        if self.images["background"] is not None:
            self.surface.blit(self.images["background"], (0, 0))
        else:
            self.surface.fill(FILL_BACKGROUND_COLOR)

        self.surface.blit(self.images['ship'], self.game.ship.rect[:2])
        self.surface.blit(self.images['fort'], self.game.fort.rect[:2])

        self.game.ship.missile_group.update()
        self.game.fort.fort_group.update()

        for missile in self.game.ship.missile_group:
            self.surface.blit(self.images['ship_missile'], missile.rect[:2])

        for missile in self.game.fort.fort_group:
            self.surface.blit(self.images['fort_missile'], missile.rect[:2])

    def update_display(self):
        if self.display is None:
            raise RuntimeError(
                "Tried to update the display, but a display hasn't been "
                "created yet! To create a display for the renderer, you must "
                "call the `make_display()` method."
            )

        self.display.blit(self.surface, [0, 0])
        pygame.display.update()
