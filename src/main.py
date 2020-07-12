import pygame

from pygame.locals import K_DOWN, K_s, K_UP, K_w, QUIT

from object.Ball import Ball
from object.Player import Player
from utils.object_position_helper import find_ball_vertical_velocity, is_out_of_screen_width

def setup_screen():
  pygame.display.set_caption(SCREEN_TITLE)
  
  return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == '__main__':
  SCREEN_COLOUR = (0, 0, 0)
  SCREEN_HEIGHT = 600
  SCREEN_TITLE = 'Pong'
  SCREEN_WIDTH = 800

  pygame.init()

  running = True
  screen = setup_screen()
  screen_middle_y = SCREEN_HEIGHT / 2
  player1 = Player((SCREEN_WIDTH / 20, screen_middle_y), K_s, K_w)
  player2 = Player((SCREEN_WIDTH - SCREEN_WIDTH / 20, screen_middle_y), K_DOWN, K_UP)
  ball = Ball((SCREEN_WIDTH / 2, screen_middle_y))
  all_sprites = pygame.sprite.Group()
  players = pygame.sprite.Group()

  players.add(player1)
  players.add(player2)

  all_sprites.add(player1)
  all_sprites.add(player2)
  all_sprites.add(ball)

  clock = pygame.time.Clock()

  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
        running = False;
    
    pressed_keys = pygame.key.get_pressed()

    # Update
    player1.update(pressed_keys, SCREEN_HEIGHT)
    player2.update(pressed_keys, SCREEN_HEIGHT)
    ball.update(SCREEN_HEIGHT)

    # Draw
    screen.fill(SCREEN_COLOUR)
    
    for entity in all_sprites:
      screen.blit(entity.surf, entity.rect)
    
    if pygame.sprite.spritecollideany(ball, players):
      ball.switch_direction()
      ball.update_vertical_speed(find_ball_vertical_velocity(ball.rect.centery, player1.rect.centery)) if pygame.sprite.collide_rect(ball, player1) else ball.update_vertical_speed(find_ball_vertical_velocity(ball.rect.centery, player2.rect.centery))
        

    if is_out_of_screen_width(ball.rect, SCREEN_WIDTH):
      running = False

    pygame.display.flip()
    clock.tick(30)