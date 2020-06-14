import pygame

from pygame.locals import QUIT

from constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def setup_screen():
  pygame.display.set_caption(SCREEN_TITLE)
  
  return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == '__main__':
  pygame.init()

  running = True
  screen = setup_screen()

  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False;