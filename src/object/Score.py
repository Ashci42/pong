from constants import BLACK, WHITE

class Score():
  def __init__(self, font, score, centre):
    self.centre = centre
    self.font = font
    self.score = score

    self.define_surface()

  def define_surface(self):
    self.text = self.font.render(str(self.score), True, WHITE, BLACK)
    self.rect = self.text.get_rect(center=self.centre)

  def increment(self):
    self.score = self.score + 1
    self.define_surface()


