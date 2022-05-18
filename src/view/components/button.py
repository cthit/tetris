import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, text, size, position):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(200, 200, 200)
        pygame.draw.rect(self, image, (200, 200.200), [
                         position[0], position[1],
                         position[0]+size[0], position[1]+size[1]])
