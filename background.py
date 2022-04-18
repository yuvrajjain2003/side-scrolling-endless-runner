import pygame

class Background():
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    x0: int
    x1: int
    y: int
    speed: int

    def __init__(self):
        """Contruct scrolling background objects."""
        # TODO Load background image
        self.image = pygame.transform.scale(pygame.image.load("projects/HACK110Game/assets/court2.png"), (1200, 650)).convert()
        self.rect = self.image.get_rect()
        self.x0 = 0
        self.x1 = self.rect.width
        self.y = 0
        self.speed = 5
         
    def update(self):
        """Move the background by moving speed amount."""
        self.x0 -= self.speed
        self.x1 -= self.speed
        if self.x0 <= -self.rect.width:
            self.x0 = self.rect.width
        if self.x1 <= -self.rect.width:
            self.x1 = self.rect.width
        
    def render(self, screen):
        """Draw background object to the screen"""
        self.update()
        screen.blit(self.image, (self.x0, self.y))
        screen.blit(self.image, (self.x1, self.y))