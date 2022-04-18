"""Floor objects have a Surface, Rect, and x and y coordinates."""

import pygame


class Floor():
    """Floor class extends pygame.sprite.Sprite to allow it to be added to Sprite groups and use Sprite methods."""
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    x: int
    y: int

    def __init__(self, x: int, y: int, width: int, height: int):
        """Construct a floor object with position, width, height, and fill it with a color."""
        self.image = pygame.image.load("projects/HACK110Game/assets/carolina.png")
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.x = x 
        self.y = y

    def render(self, screen):
        """Draw the surface of the floor object to the screen at a specific location."""
        screen.blit(self.image, self.rect)