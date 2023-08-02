import pygame
from GameObjects.Ball import Ball

from GameObjects.Paddle import Paddle
from GameObjects.ScoreDisplay import ScoreDisplay

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def startGame(opponentGenome = None):
    print("##############################")
    print("press ENTER to start the game!")
    print("##############################")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_loop_running = True
    game_running = False
    clock = pygame.time.Clock()

    paddle1 = Paddle(True, SCREEN_HEIGHT, SCREEN_WIDTH)
    paddle2 = Paddle(False, SCREEN_HEIGHT, SCREEN_WIDTH)
    ball = Ball(SCREEN_HEIGHT, SCREEN_WIDTH)
    scoreDisplay = ScoreDisplay(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH)

    while game_loop_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_running = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not game_running: game_running = True

        paddle1.move(keys[pygame.K_s] - keys[pygame.K_w])
        if opponentGenome == None:
            paddle2.move(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        else:
            output = opponentGenome.calculate([paddle2.y, ball.y, abs(paddle2.x - ball.x)])
            action = output.index(max(output))
            if action == 1: paddle2.move(-1)
            elif action == 2: paddle2.move(1)

        screen.fill((0, 0, 0))
        paddle1.draw(screen)
        paddle2.draw(screen)

        if game_running:
            whatHappened, isLeft = ball.move(paddle1, paddle2)
            if whatHappened == "score":
                if not isLeft: scoreDisplay.score1 += 1
                else: scoreDisplay.score2 += 1
            
                ball.resetPosition()
                paddle1.resetPosition()
                paddle2.resetPosition()
                game_running = False

        ball.draw(screen)
        scoreDisplay.draw(screen)

        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    startGame()