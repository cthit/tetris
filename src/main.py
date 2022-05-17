import pygame
from components.button import Button

def main():
	pygame.init()
	sWidth=800
	sHeight=600
	screen=pygame.display.set_mode((sWidth,sHeight))
	image=pygame.image.load(r'resources/images/logo.png')
	isRunning=True
	b=Button(1,"hej",(100,100))
	while isRunning:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				isRunning=False
		screen.fill((0,0,0))
		screen.blit(image,(200,100))
		pygame.display.update()



if __name__=="__main__":
	main()