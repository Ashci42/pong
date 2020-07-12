import pygame
import random

from enum import Enum

class Direction(Enum):
  LEFT = 1
  RIGHT = 2

  @classmethod
  def get_random_direction(cls):
    direction = random.randint(cls.LEFT.value, cls.RIGHT.value)

    return direction
  
  @classmethod
  def get_opposite_direction(cls, direction):
    if direction == cls.LEFT:
      return cls.RIGHT
    
    return cls.LEFT

class Ball(pygame.sprite.Sprite):
  BALL_COLOUR = (255, 255, 255)
  BALL_SIZE = (25, 25)
  BALL_SPEED = 18

  def __init__(self, starting_center):
    super(Ball, self).__init__()
    self.surf = pygame.Surface(Ball.BALL_SIZE)
    self.surf.fill(Ball.BALL_COLOUR)
    self.rect = self.surf.get_rect(center=starting_center)
    self.direction = Direction.get_random_direction()
    self.vertical_speed = 0
  
  def switch_direction(self):
    self.direction = Direction.get_opposite_direction(self.direction)

  def update(self, screen_height):
    if self.direction == Direction.LEFT:
      self.rect.move_ip(-Ball.BALL_SPEED, self.vertical_speed)
    else:
      self.rect.move_ip(Ball.BALL_SPEED, self.vertical_speed)

    if self.rect.top <= 0 or self.rect.bottom >= screen_height:
      self.vertical_speed = -self.vertical_speed

  def update_vertical_speed(self, vertical_speed):
    self.vertical_speed = vertical_speed
