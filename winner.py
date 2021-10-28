import pygame

class Winner:
    """ A class to show the winner of the game """

    def __init__(self, ai_game):
        """ Create a new instance """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ai_game.settings

        self.font = pygame.font.SysFont(None, 48)

    def prep(self, winner):
        """ Prepare the text """
        self.text = self.font.render(f"{winner.title()} is the winner", True, self.settings.text_color)

        self.rect = self.text.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 2 * self.screen_rect.centery / 3

    def update_winner(self):
        """ Draw the text on the screen """
        self.screen.blit(self.text, self.rect)
