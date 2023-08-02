import pygame


class ScoreDisplay():
    def __init__(self, defScore1, defScore2, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH

        self.score1 = defScore1
        self.score2 = defScore2

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.dashedMiddleLineSegments = 15
        self.dashedMiddleLineWidth = 10

    def draw(self, screen):
        textScore1 = self.font.render(str(self.score1), True, (255, 255, 255))
        textScore1Rect = textScore1.get_rect(center=(self.SCREEN_WIDTH / 4, 50))
        screen.blit(textScore1, textScore1Rect)

        textScore2 = self.font.render(str(self.score2), True, (255, 255, 255))
        textScore2Rect = textScore1.get_rect(center=(3 * self.SCREEN_WIDTH / 4, 50))
        screen.blit(textScore2, textScore2Rect)

        # draw middle line
        middleLineSegmentHeight = self.SCREEN_HEIGHT / \
            (2 * self.dashedMiddleLineSegments - 1)
        
        for i in range(self.dashedMiddleLineSegments):
            rect = pygame.Rect((
                (self.SCREEN_WIDTH - self.dashedMiddleLineWidth) / 2,
                2 * i * middleLineSegmentHeight,
                self.dashedMiddleLineWidth,
                middleLineSegmentHeight
            ))
            pygame.draw.rect(screen, (255, 255, 255), rect)