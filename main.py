import pygame
import sys

from pygame.locals import *

from settings import Settings
from ball import Ball
from paddle import Paddle
from game_stats import Stats
from button import PlayButton
from winner import Winner
from ia import IA

class Game:
    """ A class to manage the game """
    
    def __init__(self):
        """ Create a game instance """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Pong Game")

        self.clock = pygame.time.Clock()
        
        self.paddle_right = Paddle(self, "right")
        self.paddle_left = Paddle(self, "left")

        self.stats = Stats(self) 

        self.ball = Ball(self)

        self.ia_left = IA(self, "left")
        self.ia_right = IA(self, "right")

        self.play_button = PlayButton(self)
        self.winner = Winner(self)

        self.game_active = False
        self.ia_active_left = False
        self.ia_active_right = False

    def run_game(self):
        """ Init the game loop """
        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """ Check the game events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            if event.type == KEYUP and self.game_active:
                self._check_keyup_events(event)
            if event.type == MOUSEBUTTONDOWN and not self.game_active:
                self._check_mousebuttondown_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keydown events """
        if event.key == K_UP and not self.ia_active_right:
            self.paddle_right.move_up = True
        elif event.key == K_DOWN and not self.ia_active_right:
            self.paddle_right.move_down = True
        elif event.key == K_w and not self.ia_active_left:
            self.paddle_left.move_up = True
        elif event.key == K_s and not self.ia_active_left:
            self.paddle_left.move_down = True

    def _check_keyup_events(self, event):
        """ Respond to keyup events """
        if event.key == K_UP and not self.ia_active_right:
            self.paddle_right.move_up = False
        elif event.key == K_DOWN and not self.ia_active_right:
            self.paddle_right.move_down = False
        elif event.key == K_w and not self.ia_active_left:
            self.paddle_left.move_up = False
        elif event.key == K_s and not self.ia_active_left:
            self.paddle_left.move_down = False

    def _check_mousebuttondown_events(self, event):
        """ Respond to mousebuttondown events """
        mouse_pos = event.pos        
        if self.play_button.rect.collidepoint(mouse_pos):
            self._play_button()

    def _update_screen(self):
        """ Update the screen """
        self.screen.fill(self.settings.bg_color)

        if self.game_active:
            self.stats.update_stats()

            self.ball.update_ball()

            if self.ia_active_left:
                self.ia_left.move_paddle()

            if self.ia_active_right:
                self.ia_right.move_paddle()

            self.paddle_left.update_paddle()
            self.paddle_right.update_paddle()

            self._check_lost()
        else:
            try:
                self.winner.update_winner()
            except:
                self.play_button.prep()
                self.play_button.update_button()
            else:
                self.play_button.prep(position=1.5)
                self.play_button.update_button()

        pygame.display.update()

    def _check_lost(self):
        """ Check if anyone lost """
        lost = self.ball.check_lost()
        if not lost:
            pass
        elif lost == "right":
            if self.paddle_right.number_lives == 0:
                self.winner.prep("left")
                self.game_active = False
            self._reset_all()
        else:
            if self.paddle_left.number_lives == 0:
                self.winner.prep("right")
                self.game_active = False
            self._reset_all()

    def _reset_all(self):
        """ Reset the settings, the ball and the paddles """
        pygame.time.wait(500)
        self.ball.reset_ball()
        
        self.paddle_right.reset_paddle()
        self.paddle_left.reset_paddle()

        self.settings.reset_settings()

        self.stats.prep()

    def _play_button(self):
        """ Respond if press the play button """
        self._reset_all()
        self.paddle_left.number_lives = self.settings.number_lives
        self.paddle_right.number_lives = self.settings.number_lives

        self.game_active = True

        self.stats.prep()


if __name__ == "__main__":
    ai_game = Game()
    ai_game.run_game()
