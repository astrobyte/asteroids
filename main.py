# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    from shot import Shot
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    target = player
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot:  # This checks if new_shot is not None
                shots_group.add(new_shot)
        shots_group.update(dt)
        for shot in shots_group:
            shot.draw(screen)
        for asteroid in asteroids:
            for bullet in shots_group:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
        for object in drawable:
            if object != target and object.collision(target):
                print("Game Over!")
                pygame.quit()
                return
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()