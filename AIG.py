#pip install pygame
import sys
import pygame
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events()
        ship.blitme()
        screen.fill(bg_color)
        gf.update_screen(ai_settings, screen, ship)
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
            pygame.display.flip()
        
run_game()


bg_color = (255, 102, 203)


#to make instance of settings

from settings import Settings
ai_settings = Settings()
screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
screen.fill(ai_settings.bg_color)

#Adding the Ship image
ship = Ship(screen)


#Game functions


 