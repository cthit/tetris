import pygame
from config import FONT,FONT_SIZE


class Button(pygame.sprite.Sprite):
    def __init__(self, text, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.base_font=pygame.font.SysFont("comicsansms", 20)
        self.image = pygame.Surface(size)
        self.image.fill((200, 200, 200))
        self.text=self.base_font.render(text, True, (0, 0, 0))
        self.textrect=self.text.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.text,self.textrect)
        pygame.draw.rect(self.image, (200, 200,200), [
                         position[0], position[1],
                         position[0]+size[0], position[1]+size[1]])

        self.rect=self.image.get_rect()