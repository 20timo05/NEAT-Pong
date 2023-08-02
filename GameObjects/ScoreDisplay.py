import pygame

from game import SCREEN_HEIGHT, SCREEN_WIDTH


class ScoreDisplay():
    def __init__(self, defScore1, defScore2):
        self.score1 = defScore1
        self.score2 = defScore2

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.dashedMiddleLineSegments = 15
        self.dashedMiddleLineWidth = 10

    def draw(self, screen):
        textScore1 = self.font.render(str(self.score1), True, (255, 255, 255))
        textScore1Rect = textScore1.get_rect(center=(SCREEN_WIDTH / 4, 50))
        screen.blit(textScore1, textScore1Rect)

        textScore2 = self.font.render(str(self.score2), True, (255, 255, 255))
        textScore2Rect = textScore1.get_rect(center=(3 * SCREEN_WIDTH / 4, 50))
        screen.blit(textScore2, textScore2Rect)

        # draw middle line
        middleLineSegmentHeight = SCREEN_HEIGHT / \
            (2 * self.dashedMiddleLineSegments - 1)
        
        for i in range(self.dashedMiddleLineSegments):
            rect = pygame.Rect((
                (SCREEN_WIDTH - self.dashedMiddleLineWidth) / 2,
                2 * i * middleLineSegmentHeight,
                self.dashedMiddleLineWidth,
                middleLineSegmentHeight
            ))
            pygame.draw.rect(screen, (255, 255, 255), rect)