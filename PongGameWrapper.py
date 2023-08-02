import pygame
from GameObjects.Ball import Ball

from GameObjects.Paddle import Paddle
from GameObjects.ScoreDisplay import ScoreDisplay


class PongGameWrapper():
    def __init__(self, screen, SHOW_GAME, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = screen
        self.SHOW_GAME = SHOW_GAME

        self.paddle1 = Paddle(True, SCREEN_HEIGHT, SCREEN_WIDTH)
        self.paddle2 = Paddle(False, SCREEN_HEIGHT, SCREEN_WIDTH)
        self.ball = Ball(SCREEN_HEIGHT, SCREEN_WIDTH)

        # ScoreDisplay displays amount of HITS, not the actual Score!!
        self.scoreDisplay = ScoreDisplay(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH)
    
    def trainAI(self, genome1, genome2, idx1, idx2):
        print(f"{idx1} vs. {idx2}", end="\r")
        clock = pygame.time.Clock()

        run = True
        while run:
            if self.SHOW_GAME:
              clock.tick(60)
              for event in pygame.event.get():
                  if event.type == pygame.QUIT: quit()
            
            # get game information and predict action with genome
            # input paddle.y, ball.y, x distance between ball and paddle
            output1 = genome1.calculate([self.paddle1.y, self.ball.y, abs(self.paddle1.x - self.ball.x)])
            action1 = output1.index(max(output1))

            output2 = genome2.calculate([self.paddle2.y, self.ball.y, abs(self.paddle2.x - self.ball.x)])
            action2 = output2.index(max(output2))

            # action = 0: stand still, 1 = go up, 2 = go down
            if action1 == 1: self.paddle1.move(-1)
            elif action1 == 2: self.paddle1.move(1)

            if action2 == 1: self.paddle2.move(-1)
            elif action2 == 2: self.paddle2.move(1)

            whatHappened, isLeft = self.ball.move(self.paddle1, self.paddle2)

            if whatHappened == "hit":
                if isLeft: self.scoreDisplay.score1 += 1
                else: self.scoreDisplay.score2 += 1
            elif whatHappened == "score" or self.scoreDisplay.score1 > 100:
                # once one paddle missed the ball, end this match and evaluate fitness scores
                genome1.score += self.scoreDisplay.score1
                genome2.score += self.scoreDisplay.score2
                run = False

            # draw everything on screen
            if self.SHOW_GAME:
              self.screen.fill((0, 0, 0))
              self.paddle1.draw(self.screen)
              self.paddle2.draw(self.screen)
              self.ball.draw(self.screen)
              self.scoreDisplay.draw(self.screen)

              pygame.display.update()