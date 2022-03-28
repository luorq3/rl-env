from abc import ABC
from typing import Tuple, Any

import pygame


class SpriteBase(pygame.sprite.Sprite, ABC):

    def __init__(self,
                 image: pygame.Surface,
                 screen_size: Tuple[int, int],
                 size: Tuple[int, int],
                 rect: Tuple[int, int]):
        super(SpriteBase, self).__init__()
        self.image = image
        self.screen_size = screen_size
        self.size = size
        self.rect = image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.max_rect = [rect - size for size, rect in zip(self.size, self.screen_size)]

    def update(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError(f"Tried to call `{self.image.__class__}.update()`,"
                                  f" but it hasn't been implemented yet!")




