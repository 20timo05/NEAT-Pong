import pygame

from game import SCREEN_HEIGHT, SCREEN_WIDTH


class Paddle():
    def __init__(self, isLeft):
        self.width = 10
        self.height = 150

        self.x = 30 if isLeft else SCREEN_WIDTH - self.width - 30
        self.resetPosition()

        self.color = (255, 255, 255)

        self.speed = 4

    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, rect)

    def move(self, dir):
        self.y += dir * self.speed
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
    
    def resetPosition(self):
        self.y = (SCREEN_HEIGHT - self.height) / 2