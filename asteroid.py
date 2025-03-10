import pygame
import random
from circleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from explode import Explosion
from explode import EXPLODE_MIN_RADIUS

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

    def explode(self):
        count = random.randint(3, 12)

        for i in range(0, count):
            random_angle = random.uniform(0, 360)
            new_velocity = self.velocity.rotate(random_angle)
            new_radius = random.randint(EXPLODE_MIN_RADIUS, 10)

            projectile = Explosion(self.position.x, self.position.y, new_radius)
            projectile.velocity = new_velocity * 5

    def split(self):
        self.kill()
        self.explode()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radii = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid.velocity = new_velocity1 * 1.5
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid.velocity = new_velocity2 * 1.5
        
    def handle_asteroid_collisions(asteroids):
        asteroid_list = asteroids.sprites()
        
        ast_len = len(asteroid_list)
        for i in range(ast_len):
            for j in range(i + 1, ast_len):
                asteroid1 = asteroid_list[i]
                asteroid2 = asteroid_list[j]

                if asteroid1.checkCollisions(asteroid2):
                    asteroid1.velocity, asteroid2.velocity = -asteroid1.velocity, -asteroid2.velocity

                    overlap = (asteroid1.radius + asteroid2.radius) - asteroid1.position.distance_to(asteroid2.position)
                    if overlap > 0:
                        direction = asteroid1.position - asteroid2.position
                        if direction.length() > 0:
                            direction.normalize_ip()

                            asteroid1.position += direction * (overlap / 2)
                            asteroid2.position -= direction * (overlap / 2)
