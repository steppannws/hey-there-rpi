import pygame
from pygame.locals import *
import sys
import time
import subprocess
import logging

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Meeting Place")
    pygame.display.toggle_fullscreen()
    pygame.mouse.set_visible(False)
    
    print"Starting Meeting Place"

    while True:
        for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
					subprocess.call(['omxplayer', 'reel.mp4'])

if __name__ == "__main__":
    main()

#subprocess.call(['omxplayer', 'reel.mp4'])
