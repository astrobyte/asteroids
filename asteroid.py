import pygame
from constants import ASTEROID_SPAWN_RATE, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
from circleshape import CircleShape
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2

        

