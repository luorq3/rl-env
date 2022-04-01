from typing import Tuple

import pygame

# Sea blue
FILL_BACKGROUND_COLOR = (135, 206, 235)
# Black
# FILL_BACKGROUND_COLOR = (0, 0, 0)


def _get_render_rect(rect):
    """
    surface 的坐标(0,0)位于右上角，在渲染时需要调整至surface中央
    """
    return [i-j/2 for i, j in zip(rect[:2], rect[2:])]


class FightRenderer:

    def __init__(self, images, screen_size: Tuple[int, int]):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        self.display = None
        self.surface = pygame.Surface(screen_size)

        self.images = images

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

        self.surface.blit(self.images['ship'], _get_render_rect(self.game.ship.rect))
        self.surface.blit(pygame.transform.rotate(self.images['fort'], self.game.fort.angle),
                          _get_render_rect(self.game.fort.rect))

        self.game.ship.missile_group.update()
        self.game.fort.missile_group.update()

        for missile in self.game.ship.missile_group:
            self.surface.blit(self.images['ship_missile'], _get_render_rect(missile.rect))

        for missile in self.game.fort.missile_group:
            self.surface.blit(pygame.transform.rotate(self.images['fort_missile'], self.game.fort.angle),
                              _get_render_rect(missile.rect))

    def update_display(self):
        if self.display is None:
            raise RuntimeError(
                "Tried to update the display, but a display hasn't been "
                "created yet! To create a display for the renderer, you must "
                "call the `make_display()` method."
            )

        self.display.blit(self.surface, [0, 0])
        pygame.display.update()
