import pygame
from CONSTANTS import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = (updatable,)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()
                    break

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
