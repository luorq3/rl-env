import pygame
from fight_env_gym.envs.sprites.fort_shell import FortShell

IMAGE_PATH = '../assets/fort.png'

class Fort(pygame.sprite.Sprite):
    def __init__(self, bg_size, position):
        super(Fort, self).__init__()
        self.bg_size = bg_size
        self.image = pygame.image.load(IMAGE_PATH)
        # self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.defense = 3

    def handle(self, fort_shell_sprites, all_sprites):
        fort_shell = FortShell(self.bg_size, (self.rect.x, self.rect.y))
        fort_shell_sprites.add(fort_shell)
        all_sprites.add(fort_shell)
