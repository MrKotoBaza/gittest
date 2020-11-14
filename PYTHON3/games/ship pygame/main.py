import sys
import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from ship import Ship
from pygame.sprite import Group
from button import Button
from scorebroad import ScoreBroad


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    sb = ScoreBroad(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, sb, stats )

run_game()
