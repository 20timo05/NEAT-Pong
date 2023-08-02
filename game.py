import pygame
from GameObjects.Ball import Ball

from GameObjects.Paddle import Paddle
from GameObjects.ScoreDisplay import ScoreDisplay

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_loop_running = True
game_running = False
clock = pygame.time.Clock()

paddle1 = Paddle(True)
paddle2 = Paddle(False)
ball = Ball()
scoreDisplay = ScoreDisplay(0, 0)

while game_loop_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game_running: game_running = True

    paddle1.move(keys[pygame.K_s] - keys[pygame.K_w])
    paddle2.move(keys[pygame.K_DOWN] - keys[pygame.K_UP])

    screen.fill((0, 0, 0))
    paddle1.draw(screen)
    paddle2.draw(screen)

    if game_running:
        pointScored = ball.move(paddle1, paddle2)
        if pointScored == -1: scoreDisplay.score1 += 1
        elif pointScored == 1: scoreDisplay.score2 += 1
        if pointScored in [-1, 1]:
            ball.resetPosition()
            paddle1.resetPosition()
            paddle2.resetPosition()
            game_running = False

    ball.draw(screen)
    scoreDisplay.draw(screen)

    pygame.display.update()


pygame.quit()
