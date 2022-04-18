import pygame
import sys
from background import Background
from player import Player
from floor import Floor
from obstacles import Missile, Laser
from random import randint
from coins import Coin
pygame.font.init()
pygame.mixer.init()

WHITE = (255, 255, 255)

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 650
FLOOR_HEIGHT: int = 90

MAX_MISSILES = 2

WINNER_FONT = pygame.font.SysFont("comicsans", 100)
SCORE_FONT = pygame.font.SysFont("comicsans", 40)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Instantiate the background
background:Background = Background()

# Floor
floor: Floor = Floor(0, SCREEN_HEIGHT - FLOOR_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT)

# Something
platforms: list[pygame.rect.Rect] = [floor.rect] #floor.rect

# Instantiate the Player
player: Player = Player(100, 100, 40, 40, platforms)

# List of Missiles
missile1: Missile = Missile(1100, randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT), 46, 34)
missile2: Missile = Missile(1300, randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT), 46, 34)
missile3: Missile = Missile(1200, randint(0, SCREEN_HEIGHT - FLOOR_HEIGHT), 46, 34)
laser1: Laser = Laser()
laser2: Laser = Laser()

# Coins
coin1: Coin = Coin()
coin2: Coin = Coin()
coin3: Coin = Coin()

# Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(missile1, missile2, missile3, laser1, laser2)

# Coin Sprite Groups
coins = [coin1.rect, coin2.rect, coin3.rect]

# Playing Music
pygame.mixer.music.load('projects/HACK110Game/assets/Undertale_Megalovania.mp3')
pygame.mixer.music.play(-1, 0.0)

def draw_score(score: int, points: int, screen):
    score_text = SCORE_FONT.render("Distance: " + str(score), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
    point_text = SCORE_FONT.render("Points: " + str(points), True, WHITE)
    screen.blit(point_text, (SCREEN_WIDTH - score_text.get_width() - 10, 50))


def main():
    points: int = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quitting the loop if this condition is met
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.gravity_off()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.gravity_on()
            if missile1.rect.x <= randint(-1000, -200):
                missile1.reinit()
            if missile2.rect.x <= randint(-1000, -200):
                missile2.reinit()
            if missile3.rect.x <= randint(-1000, -200):
                missile3.reinit()
            if laser1.rect.x <= 0:
                laser1.reinit()
            if laser2.rect.x <= 0:
                laser2.reinit()
            if coin1.rect.x <= 0:
                coin1.reinit()
            if coin2.rect.x <= 0:
                coin2.reinit()
            if coin3.rect.x <= 0:
                coin3.reinit()
            

        # The background
        background.render(screen)

        # The player
        player.render(screen)

        # The floor
        floor.render(screen)

        # The Missiles
        missile1.render(screen)
        missile2.render(screen)
        missile3.render(screen)
        
        # The laser
        laser1.render(screen)
        laser2.render(screen)

        # Coins
        coin1.render(screen)
        coin2.render(screen)
        coin3.render(screen)
        
        # Score:
        draw_score(pygame.time.get_ticks() // 50, points, screen)

        if pygame.sprite.spritecollideany(player, enemies):
            missile1.reinit()
            missile2.reinit()
            missile3.reinit()
            laser1.reinit()
            laser2.reinit()
            coin1.reinit()
            coin2.reinit()
            coin3.reinit()
            
            # End the game if there's a collision
            player.end_game(screen)

        if player.rect.colliderect(coin1.rect):
            coin1.reinit()
            points += 1

        elif player.rect.colliderect(coin2.rect):
            coin2.reinit()
            points += 1

        elif player.rect.colliderect(coin3.rect):
            coin3.reinit()
            points += 1

        pygame.display.flip()
        clock.tick(60)  # The frame rate

    main()

if __name__ == "__main__":
    main()