import pygame


class Paddle():
    def __init__(self, isLeft, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH

        self.width = 10
        self.height = 150

        self.x = 0 if isLeft else self.SCREEN_WIDTH - self.width
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
        elif self.y + self.height > self.SCREEN_HEIGHT:
            self.y = self.SCREEN_HEIGHT - self.height
    
    def resetPosition(self):
        self.y = (self.SCREEN_HEIGHT - self.height) / 2