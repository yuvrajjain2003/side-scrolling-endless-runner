"""A Class for Obstacles."""

import pygame
from pygame.locals import RLEACCEL
from random import randint

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 650
FLOOR_HEIGHT: int = 90


class Missile(pygame.sprite.Sprite):
    """A trash class for a Dook Devil Missile."""
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    vel: int = 20

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """Constructor takes x and y as coordinates and height and width to draw the missile rect."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("projects/HACK110GAME/assets/missile.png"), (146, 134)).convert()
        self.rect = pygame.rect.Rect(x, y, height, width)
        self.image.set_colorkey((0, 0, 0), RLEACCEL)

    def move_vel(self):
        self.rect.x -= self.vel
    
    def render(self, screen):
        self.move_vel()
        screen.blit(self.image, self.rect)
    
    def reinit(self):
        self.rect.x = 1300
        self.rect.y = randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT)


class Laser(pygame.sprite.Sprite):
    rect: pygame.rect.Rect
    speed: int
    surface: pygame.surface.Surface
    x_value: int
    y_value: int
    height: int

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x_value = randint(1200, 1500)
        y_value = randint(100, 500)
        height = randint(100, 150)
        self.rect = pygame.Rect(x_value, y_value, 20, height)
        self.speed = 5
        self.surface = pygame.transform.scale(pygame.image.load("projects/HACK110GAME/assets/laser.png"), (20, height)).convert()
        self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
    
    def update(self):
        self.rect.x -= self.speed

    def render(self, screen):
        self.update()
        screen.blit(self.surface, (self.rect.x, self.rect.y))

    def reinit(self):
        self.rect.x = randint(1200, 1500)
        self.rect.y = randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT)


