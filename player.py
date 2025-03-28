import pygame
import sys
from circleShape import CircleShape
from shoot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED

PLAYER_SHOOT_COOLDOWN = 0.15
PLAYER_LINE_WIDTH = 2
PI = 3.1415927

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), PLAYER_LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360

    def update(self, dt):
        self.cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot(dt)
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def shoot(self, dt):
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(self.rotation)
        velocity = PLAYER_SHOT_SPEED * velocity * dt
        shot = Shot(self.position.x, self.position.y, self.radius, velocity)

    def move(self, dt):
        move_vector = pygame.Vector2(0, 1)
        move_vector = move_vector.rotate(self.rotation)

        move_vector = move_vector * PLAYER_SPEED * dt

        self.position += move_vector

        #No need to manually handle the math dummy.....
        #deg_radian = self.rotation * PI / 180
        #selfCos = cmath.cos(deg_radian)
        #selfSin = cmath.sin(deg_radian)

        #move_vector = pygame.Vector2(0, 1)
        #new_x = move_vector.x * selfCos - move_vector.y * selfSin
        #new_y = move_vector.x * selfSin + move_vector.y * selfCos

        #offset_x = PLAYER_SPEED * dt * new_x
        #offset_y = PLAYER_SPEED * dt * new_y

        #print(f"X: {offset_x}, Y: {offset_y}")

        #move_vector = pygame.Vector2(new_x, new_y)

        #self.position = self.position + move_vector
