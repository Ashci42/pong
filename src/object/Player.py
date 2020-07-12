import pygame

from constants import PLAYER_HEIGHT, WHITE

class Player(pygame.sprite.Sprite):
  PLAYER_COLOUR = WHITE
  PLAYER_HORIZONTAL_SPEED = 0
  PLAYER_SIZE = (25, PLAYER_HEIGHT)
  PLAYER_VERTICAL_SPEED = 10

  def __init__(self, starting_center, down_key, up_key):
    super(Player, self).__init__()
    
    self.starting_center = starting_center
    self.surf = pygame.Surface(Player.PLAYER_SIZE)
    self.down = down_key
    self.up = up_key

    self.surf.fill(Player.PLAYER_COLOUR)
    self.set_initial_state()
  
  def reset_to_initial_state(self):
    self.set_initial_state()

  def set_initial_state(self):
    self.rect = self.surf.get_rect(center=self.starting_center)

  def update(self, pressed_keys, screen_height):
    if pressed_keys[self.down]:
        self.rect.move_ip(Player.PLAYER_HORIZONTAL_SPEED, Player.PLAYER_VERTICAL_SPEED)
    if pressed_keys[self.up]:
        self.rect.move_ip(Player.PLAYER_HORIZONTAL_SPEED, -Player.PLAYER_VERTICAL_SPEED)
    
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= screen_height:
        self.rect.bottom = screen_height