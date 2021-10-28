import pygame

class PlayButton:
    """ A class to create a play button """

    def __init__(self, ai_game):
        """ Create a new play button """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ai_game.settings

        self.font = pygame.font.SysFont(None, 48)

    def prep(self, position=1):
        """ Prepare the play button """
        self.text = self.font.render("Play", True, self.settings.text_color)
        
        self.rect = self.text.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery * position

    def update_button(self):
        """ Draw the play button on the screen """
        self.screen.blit(self.text, self.rect)
