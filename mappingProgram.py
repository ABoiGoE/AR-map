# Python program to move the image
# with the mouse

# Import the library pygame
import pygame
from pygame.locals import *

# Points on the map
points = [(5299575, 3863423), (5431315, 3702398)]

# Take colors input
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Construct the GUI
pygame.init()

# Set dimensions of GUI
w, h = 1600, 800
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)

# Set variables for the maps
roadMap = pygame.image.load('eagle/Roads.jpg')
roadMap.convert()

topoMap = pygame.image.load('eagle/Topo.png')
topoMap.convert()

# Setting up the GPS coordinates
topLeft = 5299575, 3863423
bottomRight = 5431315, 3702398

# Draw rectangle around the maps
roadRect = roadMap.get_rect()
roadRect.center = w//2, h//2

topoRect = topoMap.get_rect()
topoRect.center = w//2, h//2

# Set running and moving values
running = True
moving = False

# Set wether the topographical or the road map is being displayed
roadDisplay = True

# Setting what happens when map
# is in running state
while running:
	
	for event in pygame.event.get():

		# Close if the user quits the
		# map
		if event.type == QUIT:
			running = False

		# Making the maps move
		elif event.type == MOUSEBUTTONDOWN:
			if roadDisplay:
				if roadRect.collidepoint(event.pos):
					moving = True
			else:
				if topoRect.collidepoint(event.pos):
					moving = True

		# Set moving as False if you want
		# to move the image only with the
		# mouse click
		# Set moving as True if you want
		# to move the image without the
		# mouse click
		elif event.type == MOUSEBUTTONUP:
			moving = False

		# Make your image move continuously
		elif event.type == MOUSEMOTION and moving:
			if roadDisplay:
				roadRect.move_ip(event.rel)
			else:
				topoRect.move_ip(event.rel)
		
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				if roadDisplay:
					roadDisplay = False
				else:
					roadDisplay = True

	# Set screen color and image on screen
	screen.fill((0, 0, 0))
	if roadDisplay:
		screen.blit(roadMap, roadRect)
		pygame.draw.rect(screen, BLUE, roadRect, 2)
	else:
		screen.blit(topoMap, topoRect)
		pygame.draw.rect(screen, BLUE, topoRect, 2)

	for point in points:
		pygame.draw.circle(screen, YELLOW, ((point[0] - topLeft[0]) / (bottomRight[0] - topLeft[0]) * (topoRect.right - topoRect.left) + topoRect.left, (point[1] - topLeft[1]) / (bottomRight[1] - topLeft[1]) * (topoRect.bottom - topoRect.top) + topoRect.bottom), 4)

	# getting the coordinates of the map
	coords = [roadRect.x, roadRect.y]
	print(coords)

	# Update the GUI pygame
	pygame.display.flip()

# Quit the GUI game
pygame.quit()
