from constants import MAX_BALL_VERTICAL_SPEED, PLAYER_HEIGHT

def find_ball_vertical_velocity(ball_centre, player_center):
  diff = ball_centre - player_center

  if diff == 0:
    return 0

  percentage = diff / PLAYER_HEIGHT

  return MAX_BALL_VERTICAL_SPEED * percentage
  
def is_out_of_screen_width(rect, width):
  return True if rect.left <= 0 or rect.right >= width else False

