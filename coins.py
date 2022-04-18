"""Coins and Score Implementation."""

import pygame
from pygame.locals import RLEACCEL
from random import randint

SCREEN_HEIGHT: int = 650
FLOOR_HEIGHT: int = 90

class Coin(pygame.sprite.Sprite):
    """Implements coins duh."""
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    vel: int
    x_value: int
    y_value: int

    def __init__(self):
        """Intializes coins."""
        x_value = 800
        y_value = randint(100, 500)
        self.vel = 5
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("projects/HACK110GAME/assets/bball.png"), (34, 34)).convert()
        self.rect = pygame.rect.Rect(x_value, y_value, 32, 30)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)

    def update(self):
        self.rect.x -= self.vel
    
    def render(self, screen):
        self.update()
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def reinit(self):
        self.rect.x = randint(1200, 1500)
        self.rect.y = randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT)