import pygame
from circleShape import CircleShape

ASTEROID_LINE_WIDTH = 2

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
