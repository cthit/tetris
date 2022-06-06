
import pygame
from config import PLAY_WIDTH, BUTTON_COLOUR,BLOCK_SIZE,PLAY_HEIGHT,WIDTH,LOCKED_COLOUR
from controller.Observer import Observer
from enum import Enum

class dir(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class BaseTetromino(pygame.sprite.Sprite, Observer):
    def __init__(self,position,layout,size):
        pygame.sprite.Sprite.__init__(self)
        self.rot=1
        self.layout=layout
        self.size=size
        self.createImage()
        self.createRect(position)
        self.locked=False


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


    def createImage(self):
        self.colour=BUTTON_COLOUR
        self.image = pygame.Surface((BLOCK_SIZE*self.size[0], BLOCK_SIZE*self.size[1])).convert_alpha()
        self.image.fill((0,0,0,0))

    def createRect(self,position):
        self.blockify()
        self.rect=pygame.draw.lines(self.image,self.colour,False,self.layout,width=2*BLOCK_SIZE)
        self.rect.x=position[0]
        self.rect.y=position[1]

    def blockify(self):
        self.layout = [(x*BLOCK_SIZE,y*BLOCK_SIZE) for x,y in self.layout]

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
        self.rot=(self.rot+1)%2
        posX=self.rect.x
        posY=self.rect.y
        self.image=pygame.transform.rotate(self.image,90)
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        while self.isOutside(dir.LEFT):
            self.rect.x=self.rect.x+BLOCK_SIZE
        while self.isOutside(dir.RIGHT):
            self.rect.x=self.rect.x-BLOCK_SIZE

    def checkToMove(self,dir):
        return not self.isOutside(dir)

    def isOutside(self,dir):
        middle=WIDTH/2
        fieldWidth=PLAY_WIDTH/2
        match dir:
            case dir.DOWN:
                if self.rect.y+BLOCK_SIZE*self.size[self.rot]>PLAY_HEIGHT:
                    self.locked=True
                    return True
            case dir.LEFT:
                if self.rect.x-BLOCK_SIZE<middle-fieldWidth:
                    return True
            case dir.RIGHT:
                if self.rect.x+BLOCK_SIZE*self.size[(self.rot+1)%2]>middle+fieldWidth:
                    return True
            case dir.UP:
                return self.isOutside(dir.RIGHT)|self.isOutside(dir.LEFT)
        return False

    def getPosition(self):
        retList=[]
        print(self.layout)
        for x,y in self.layout:
            retList.append([(int)(x/BLOCK_SIZE)+(int)((self.rect.x-PLAY_WIDTH)/BLOCK_SIZE)-6,(int)(y/BLOCK_SIZE)+(int)(self.rect.y/BLOCK_SIZE)])
        print(retList)
        return retList