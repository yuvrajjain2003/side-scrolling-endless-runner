"""The Player class lives here. Player objects include a Surface, Rect, and logic for moving left, right, and jumping on other Surfaces."""

import pygame
from pygame.locals import RLEACCEL

pygame.font.init()

WINNER_FONT = pygame.font.SysFont("comicsans", 100)

SCREEN_HEIGHT: int = 650
SCREEN_WIDTH: int = 1200

FLOOR_HEIGHT: int = 90
PLAYER_HEIGHT: int = 58
PLAYER_WIDTH: int = 44

WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    """The Player extends pygame.sprite.Sprite to take advantage of builtin Sprite methods."""
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    movey: int
    is_boosting: bool
    is_falling: bool = True
    collision_list: list[pygame.rect.Rect]
    vel: int
    acceleration: int
    max_vel: int

    def __init__(self, x: int, y: int, width: int, height: int, collision_list: list[pygame.rect.Rect]):
        """Constructor takes x and y as coordinates, height and width for the size and a list of Rects (rectangles) the player could collide with."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("projects/HACK110Game/assets/barry.png"), (44, 58)).convert()
        self.rect = pygame.rect.Rect(x, y, height, width)
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.vel = 0
        self.acceleration = 1
        self.max_vel = 12

    def update(self):
        """This is called every frame to check for collisions with the floor and apply boosting movement."""    
        if self.is_falling and self.rect.y <= SCREEN_HEIGHT - FLOOR_HEIGHT - PLAYER_HEIGHT:
            self.rect.y += 5
            self.vel = 0
        elif self.is_falling and self.rect.y > SCREEN_HEIGHT - FLOOR_HEIGHT - PLAYER_HEIGHT:
            self.rect.y += 0
            self.vel = 0
        elif not(self.is_falling) and self.rect.y < 0:
            self.rect.y += 0
        elif not(self.is_falling) and self.rect.y > 0:
            self.rect.y -= min(self.vel + self.acceleration, self.max_vel)
            self.vel += self.acceleration
    
    def gravity_on(self):
        """Turns on the 'gravity' only when the player object should be falling."""
        self.is_falling = True


    def gravity_off(self):
        """Turns off the 'gravity'."""
        self.is_falling = False

    def render(self, screen) -> None:
        """Draw surface of player onto the screen at its rect location."""
        self.update()
        screen.blit(self.image, self.rect)
    
    def end_game(self, screen):
        draw_text = WINNER_FONT.render("GIT GUD NOOB!", True, WHITE)
        screen.blit(draw_text, (SCREEN_WIDTH // 2 - draw_text.get_width()/2, SCREEN_HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
