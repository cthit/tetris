import pygame
import keyboard
from config import STANDARD_FONT,FONT_SIZE,BUTTON_COLOUR,BLOCK_SIZE
from controller.Observer import Observer


class BaseTetromino(pygame.sprite.Sprite, Observer):
    def __init__(self, text, position):
        pygame.sprite.Sprite.__init__(self)
        self.createImage(text)
        self.createRect(position)
        self.setupKeyboard()

    def update(self):
        self.down(None)

    def createImage(self,text):
        self.base_font=pygame.font.SysFont(STANDARD_FONT, FONT_SIZE)
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(BUTTON_COLOUR)
        #Text is temporary
        self.text=self.base_font.render(text, True, (0, 0, 0))
        self.textrect=self.text.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.text,self.textrect)

    def createRect(self,position):
        self.rect=self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]

    def setupKeyboard(self):
        keyboard.on_press_key('a', self.left)
        keyboard.on_press_key('d', self.right)
        keyboard.on_press_key('s', self.down)
        keyboard.on_press_key('space', self.rotate)

    def down(self, event):
        self.rect.y=self.rect.y+BLOCK_SIZE

    def left(self, event):
        self.rect.x=self.rect.x-BLOCK_SIZE

    def right(self, event):
        self.rect.x=self.rect.x+BLOCK_SIZE

    def rotate(self, event):
        posX=self.rect.x
        posY=self.rect.y
        self.image=pygame.transform.rotate(self.image,90)
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY