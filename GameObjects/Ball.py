import random
import pygame

class Ball():
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH

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

        if self.x < 0: return ("score", True)
        elif self.x + self.width > self.SCREEN_WIDTH: return ("score", False)

        for paddle in [paddle1, paddle2]:
            # check collision with paddle
            if self.__checkCollision(paddle):
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
                if abs(self.yVel) < 0.5:
                    self.yVel = 0.5 if self.yVel >= 0 else -0.5

                # each collision with paddle, xVel increases a little
                self.xVel = self.xVel + 0.1 if self.xVel > 0 else self.xVel - 0.1
                # ensure that it does not exceed max velocity of 8
                self.xVel = max(min(self.xVel, 8), -8)

                # move ball so that it can freely move again
                while self.__checkCollision(paddle): self.x += self.xVel

                return ("hit", paddle == paddle1)

        if self.y < 0 or self.y + self.height > self.SCREEN_HEIGHT:
            self.yVel = -self.yVel
        
        # move ball so that it can freely move again
        while self.y < 0 or self.y + self.height > self.SCREEN_HEIGHT:
            self.y += self.yVel

        return ("nothing", True)

    def resetPosition(self):
        self.xVel = random.choice([-4, 4])
        self.yVel = random.choice([random.uniform(1, 5), random.uniform(-5, -1)])
        self.x = (self.SCREEN_WIDTH - self.width) / 2
        self.y = (self.SCREEN_HEIGHT - self.height) / 2

    def __checkCollision(self, paddle):
        return not (self.x + self.width < paddle.x or
                    self.y + self.height < paddle.y or
                    self.x > paddle.x + paddle.width or
                    self.y > paddle.y + paddle.height)