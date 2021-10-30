class IA:

    def __init__(self, ai_game, position):
        """ Create a new IA """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.paddle= ai_game.paddle_left if position == "left" else ai_game.paddle_right
        self.paddle_rect = self.paddle.rect
        self.ball = ai_game.ball
        self.ball_rect = self.ball.rect

    def move_paddle(self):
        """ Move the paddle """
        if self.ball_rect.centery > self.paddle_rect.bottom and self.paddle_rect.bottom < self.settings.screen_height:
            self.paddle.move_down = True
        else:
            self.paddle.move_down = False
        if self.ball_rect.centery < self.paddle_rect.top and self.paddle_rect.bottom > 0:
            self.paddle.move_up = True
        else:
            self.paddle.move_up = False
