import random
import pygame

from game import SCREEN_HEIGHT, SCREEN_WIDTH


class Ball():
    def __init__(self):
        self.width = 10
        self.height = 10

        self.resetPosition()

        self.color = (255, 255, 255)

    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, rect)

    def move(self, paddle1, paddle2):
        # move based on angle and velocity
        self.x += self.xVel
        self.y += self.yVel

        if self.x < 0: return -1
        elif self.x + self.width > SCREEN_WIDTH: return 1

        for paddle in [paddle1, paddle2]:
            # check collision with paddle
            if not (self.x + self.width < paddle.x or
                    self.y + self.height < paddle.y or
                    self.x > paddle.x + paddle.width or
                    self.y > paddle.y + paddle.height):
                self.xVel = -self.xVel

                # adjust yVel based on where paddle hit ball
                ymin = paddle.y - self.height
                ymax = paddle.y + paddle.height

                # shift interval, so that ymin = 0
                norm_y = self.y - ymin
                norm_ymax = ymax - ymin

                # get percentage where ball hit player
                perc = norm_y / norm_ymax

                self.yVel = (perc - 0.5) * 8

                # each collision with paddle, xVel increases a little
                self.xVel = self.xVel + 0.1 if self.xVel > 0 else self.xVel - 0.1
                # ensure that it does not exceed max velocity of 8
                self.xVel = max(min(self.xVel, 8), -8)

        if self.y < 0 or self.y + self.height > SCREEN_HEIGHT:
            self.yVel = -self.yVel

        return 0

    def resetPosition(self):
        self.xVel = random.choice([-4, 4])
        self.yVel = random.random() * 4 - 2
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = (SCREEN_HEIGHT - self.height) / 2