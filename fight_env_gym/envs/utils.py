import os
from pathlib import Path
from typing import List, Dict, Any

from pygame import image as pyg_image
from pygame import Rect


_BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent

SPRITES_PATH = str(_BASE_DIR / 'assets')


def pixel_collision(rect1: Rect,
                    rect2: Rect,
                    hitmask1: List[List[bool]],
                    hitmask2: List[List[bool]]) -> bool:
    rect = rect1.clip(rect2)
    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.y - rect2.y, rect.y - rect2.y

    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False


def get_hitmask(image) -> List[List[bool]]:
    mask = []
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x, y))[3]))
    return mask


def _load_sprite(filename, convert, alpha=True):
    img = pyg_image.load(f"{SPRITES_PATH}/{filename}")
    return (img.convert_alpha() if convert and alpha
            else img.convert() if convert
            else img)


def load_images(convert: bool = True) -> Dict[str, Any]:
    images = {}

    try:
        images["ship"] = _load_sprite("ship.png", convert=convert, alpha=True)
        images["fort"] = _load_sprite("fort.png", convert=convert, alpha=True)
        images["background"] = None
        images["ship_missile"] = _load_sprite("ship_missile.png", convert=convert, alpha=True)
        images["fort_missile"] = _load_sprite("fort_missile.png", convert=convert, alpha=True)

    except FileNotFoundError as ex:
        raise FileNotFoundError("Can't find the sprites folder! No such file or"
                                f"directory: {SPRITES_PATH}") from ex
    return images

def load_image(filename, convert: bool = True) -> Any:
    try:
        image = _load_sprite(f"{filename}.png", convert=convert, alpha=True)
    except FileNotFoundError as ex:
        raise FileNotFoundError("Can't find the sprites folder! No such file or"
                                f"directory: {SPRITES_PATH}") from ex
    return image
