import sys

import pygame
from fight_env_gym.envs.sprites import Ship
from fight_env_gym.envs.sprites import Fort

WIDTH = 700
HEIGHT = 512
SIZE = (WIDTH, HEIGHT)
FPS = 30
BG = (135, 206, 235)

all_sprites = pygame.sprite.Group()
ship_sprites = pygame.sprite.Group()
fort_sprites = pygame.sprite.Group()
ship_shell_sprites = pygame.sprite.Group()
fort_shell_sprites = pygame.sprite.Group()

FORT_LAUNCH_EVENT = pygame.USEREVENT
SHIP_LAUNCH_EVENT = pygame.USEREVENT + 1


def make_ship():
    ship = Ship(SIZE, (0, 256))
    ship_sprites.add(ship)
    all_sprites.add(ship)
    return ship


def make_fort():
    fort = Fort(SIZE, (650, 256))
    fort_sprites.add(fort)
    all_sprites.add(fort)
    return fort


def collide_check(sprite, group):
    collided = pygame.sprite.spritecollide(sprite, group, True)
    sprite.defense -= len(collided)
    return sprite.defense


# def main():
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Fight")
clock = pygame.time.Clock()

ship = make_ship()
fort = make_fort()

pygame.time.set_timer(FORT_LAUNCH_EVENT, 1000)
pygame.time.set_timer(SHIP_LAUNCH_EVENT, 50)

running = True
while running:
    clock.tick(FPS)

    key_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == FORT_LAUNCH_EVENT:
            fort.handle(fort_shell_sprites, all_sprites)
        elif event.type == SHIP_LAUNCH_EVENT:
            ship.handle(key_pressed, ship_shell_sprites, all_sprites)

    ship_defense = collide_check(ship, fort_shell_sprites)
    if ship_defense <= 0:
        print("GAME OVER!")
        running = False
    fort_defense = collide_check(fort, ship_shell_sprites)
    if fort_defense <= 0:
        print("WIN!")
        running = False

    all_sprites.update()
    screen.fill(BG)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
# sys.exit()


# if __name__ == '__main__':
#     main()
