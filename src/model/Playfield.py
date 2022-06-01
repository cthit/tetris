import pygame
from controller.Observer import Observer
from config import PLAY_HEIGHT, PLAY_WIDTH, BLOCK_SIZE, WIDTH


class Playfield(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (PLAY_WIDTH + 2 * BLOCK_SIZE,
             PLAY_HEIGHT + 2 * BLOCK_SIZE)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        height = PLAY_HEIGHT + 2 * BLOCK_SIZE
        width = PLAY_WIDTH + 2 * BLOCK_SIZE
        self.rect = pygame.draw.lines(self.image, (255, 255, 255),
                                      True, [(0, 0), (0, height),
                                             (width, height), (width, 0)],
                                      width=2 * BLOCK_SIZE)
        self.rect.x = WIDTH / 2 - width / 2
