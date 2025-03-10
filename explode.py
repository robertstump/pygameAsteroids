import pygame
from circleShape import CircleShape

EXPLODE_MIN_RADIUS = 4
EXPLODE_LINE_WIDTH = 2

class Explosion(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, EXPLODE_LINE_WIDTH)
