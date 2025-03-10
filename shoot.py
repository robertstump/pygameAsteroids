import pygame
from circleShape import CircleShape
from constants import SHOT_RADIUS

SHOT_LINE_WIDTH = 2

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = SHOT_RADIUS
        self.velocity = velocity 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity

