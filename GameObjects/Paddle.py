import pygame


class Paddle():
    def __init__(self, isLeft, SCREEN_HEIGHT, SCREEN_WIDTH, showInput=False):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.showInput = showInput

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 10) if showInput else None
        self.lastMove = None
        
        self.width = 10
        self.height = 150

        self.x = 0 if isLeft else self.SCREEN_WIDTH - self.width
        self.resetPosition()

        self.color = (255, 255, 255)

        self.speed = 4
        self.isLeft = isLeft

    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, rect)

        if self.showInput:
            keySize = 40

            xPos = self.SCREEN_WIDTH / 2 - 2 * keySize - 40
            if not self.isLeft: xPos = self.SCREEN_WIDTH / 2 + 40
            yPos = 10

            rects = [
                pygame.Rect((xPos, yPos, 2 * keySize, keySize)),
                pygame.Rect((xPos, 2 * yPos + keySize, 2 * keySize, keySize))
            ]
            
            if self.lastMove == -1: pygame.draw.rect(screen, (186, 73, 73), rects[0])
            elif self.lastMove == 1: pygame.draw.rect(screen, (186, 73, 73), rects[1])

            for idx, dir in enumerate(["Up", "Down"]):
                text = self.font.render(dir, True, (255, 255, 255))
                text_rect = text.get_rect(center=rects[idx].center)
                screen.blit(text, text_rect)
                pygame.draw.rect(screen, (255, 255, 255), rects[idx], width=3)



    def move(self, dir):
        self.y += dir * self.speed
        self.lastMove = dir
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > self.SCREEN_HEIGHT:
            self.y = self.SCREEN_HEIGHT - self.height
    
    def resetPosition(self):
        self.y = (self.SCREEN_HEIGHT - self.height) / 2
    
    def displayInput(self, screen, input):
        text = [
            f"Paddle Y-Position: {round(input[0], 3)}",
            f"Ball Y-Position: {round(input[1], 3)}",
            f"Distance between Ball & Paddle: {round(input[2], 3)}"
        ]

        # get width of longest line
        maxWidth, height = self.font.size(max(text, key=len))
        
        for idx, line in enumerate(text):
            text_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (self.SCREEN_WIDTH - maxWidth - 10, 10 + height * idx))
