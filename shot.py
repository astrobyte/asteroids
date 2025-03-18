import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    def update(self, dt):
        self.position += self.velocity * dt