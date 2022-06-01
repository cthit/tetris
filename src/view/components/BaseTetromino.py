
import pygame
#import keyboard
from config import PLAY_WIDTH, STANDARD_FONT,FONT_SIZE,BUTTON_COLOUR,BLOCK_SIZE,PLAY_HEIGHT,WIDTH,LOCKED_COLOUR
from controller.Observer import Observer
from enum import Enum

class dir(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class BaseTetromino(pygame.sprite.Sprite, Observer):
    def __init__(self, text, position):
        pygame.sprite.Sprite.__init__(self)
        self.createImage(text)
        self.createRect(position)
        self.locked=False
        #self.setupKeyboard()

    def update(self,event):
        if self.locked:
            self.colour=LOCKED_COLOUR
            return
        if event==dir.DOWN:
            self.down(None)
        if event==dir.LEFT:
            self.left(None)
        if event==dir.RIGHT:
            self.right(None)
        if event==dir.UP:
            self.rotate(None)


    def createImage(self,text):
        self.colour=BUTTON_COLOUR
        self.base_font=pygame.font.SysFont(STANDARD_FONT, FONT_SIZE)
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(self.colour)
        #Text is temporary
        self.text=self.base_font.render(text, True, (0, 0, 0))
        self.textrect=self.text.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.text,self.textrect)

    def createRect(self,position):
        self.rect=self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]

    #def setupKeyboard(self):
        #keyboard.on_press_key('a', self.left)
        #keyboard.on_press_key('d', self.right)
        #keyboard.on_press_key('s', self.down)
        #keyboard.on_press_key('space', self.rotate)

    def down(self, event):
        if self.checkToMove(dir.DOWN):
            self.rect.y=self.rect.y+BLOCK_SIZE

    def left(self, event):
        if self.checkToMove(dir.LEFT):
            self.rect.x=self.rect.x-BLOCK_SIZE

    def right(self, event):
        if self.checkToMove(dir.RIGHT):
            self.rect.x=self.rect.x+BLOCK_SIZE

    def rotate(self, event):
        posX=self.rect.x
        posY=self.rect.y
        self.image=pygame.transform.rotate(self.image,90)
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY

    def checkToMove(self,dir):
        return not self.isOutside(dir)

    def isOutside(self,dir):
        middle=WIDTH/2
        fieldWidth=PLAY_WIDTH/2
        match dir:
            case dir.DOWN:
                if self.rect.y+BLOCK_SIZE>PLAY_HEIGHT:
                    self.locked=True
                    return True
            case dir.LEFT:
                if self.rect.x-BLOCK_SIZE<middle-fieldWidth:
                    return True
            case dir.RIGHT:
                if self.rect.x+BLOCK_SIZE>middle+fieldWidth:
                    return True
        return False
