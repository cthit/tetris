import pygame


def main():
	pygame.init()
	sWidth=800
	sHeight=600
	screen=pygame.display.set_mode((sWidth,sHeight))
	isRunning=True
	while isRunning:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				isRunning=False
		screen.fill((255,255,255))



if __name__=="__main__":
	main()