import pygame
import random
import time

class Ball:
    """ A class to manage the ball """

    def __init__(self, ai_game):
        """ Create a ball """
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.paddle_right = ai_game.paddle_right
        self.paddle_left = ai_game.paddle_left

        self.image = pygame.image.load("Assets/ball.png")
        self.image = pygame.transform.scale(self.image, self.settings.ball_size)

        self.rect = self.image.get_rect()
        
        self.sound_hit = pygame.mixer.Sound("Assets/418556__14fpanskabubik-lukas__ping-pong-hit.wav")
        self.reset_ball()

    def reset_ball(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = -1

        self.dir_x = random.choice([-1,1])
        self.dir_y = -1

    def update_ball(self):
        """ Update the ball position and draw it in the screen """
        self._check_bounce_screen()
        self._check_bounce_paddles()
        self.rect.move_ip(self.dir_x*self.settings.ball_speed, self.dir_y*self.settings.ball_speed)

        self.screen.blit(self.image, self.rect)

    def _check_bounce_screen(self):
        """ Check if the ball bounces off the screen """
        if self.rect.top <= 0 or self.rect.bottom >= self.settings.screen_height:
            self.dir_y *= -1
            # A correction
            self.rect.move_ip(0, self.dir_y*self.settings.ball_speed)

    def _check_bounce_paddles(self):
        """ Check if the ball bounces off the paddles """
        if self.rect.colliderect(self.paddle_left.rect):  
            if self.just_one: 
                self._ball_bounce(self.paddle_left)
        elif self.rect.colliderect(self.paddle_right.rect):
            if self.just_one: 
                self._ball_bounce(self.paddle_right)
        else:
            self.just_one = True

    def _ball_bounce(self, paddle):
        """ Change the direction and the speed of the ball, and the speed of the paddles """
        self.just_one = False # So that the ball does not accelerate more than it should
        self.dir_y = -1 * (2/self.settings.paddle_height)*(paddle.rect.centery-self.rect.centery)
        self.dir_x *= -1
        self.settings.ball_speed *= self.settings.ball_rate 
        self.settings.paddle_speed *= self.settings.paddle_rate
        self.sound_hit.play()


    def check_lost(self):
        """ Check if anyone lost """
        if self.rect.right >= self.settings.screen_width:
            self.paddle_right.number_lives -= 1
            return "right"
        elif self.rect.left <= 0:
            self.paddle_left.number_lives -= 1
            return "left"
        return  None
