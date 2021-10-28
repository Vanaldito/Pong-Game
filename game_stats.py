import pygame

class Stats:
    """ A class to manage the game stats """

    def __init__(self, ai_game):
        """ Init the stats """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.paddle_right = ai_game.paddle_right
        self.paddle_left = ai_game.paddle_left

        self.font = pygame.font.SysFont(None, 200)

        self.prep()

    def prep(self):
        """ Prepare the text to show """
        self.text_right = self.font.render(str(3-self.paddle_left.number_lives), 
                                           True, self.settings.text_color)
        self.right_rect = self.text_right.get_rect()
        self.right_rect.centerx = 3 * self.screen_rect.centerx / 2
        self.right_rect.centery = self.screen_rect.centery

        self.text_left = self.font.render(str(3-self.paddle_right.number_lives), 
                                          True, self.settings.text_color)

        self.left_rect = self.text_left.get_rect()
        self.left_rect.centerx =  self.screen_rect.centerx / 2
        self.left_rect.centery = self.screen_rect.centery

    def update_stats(self):
        """ Draw the stats in the screen """
        self.screen.blit(self.text_right, self.right_rect)
        self.screen.blit(self.text_left, self.left_rect)
