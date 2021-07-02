import random, pygame, sys, time
from pygame.locals import *

FPS = 15
WIDTH = 720
HEIGHT = 480

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 155,   0)


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAY, BASICFONT
    
    pygame.init()
    pygame.display.set_caption('Snake :V')
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    startScreen()
    while True:
        runGame()
        gameOverScreen()

def runGame():
    # initial score
    score = 0

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit posiiton
    fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction


    # Main Function
    while True:
        
        # handling key events
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == K_ESCAPE:
                    terminate()

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (WIDTH // 10)) * 10,
                            random.randrange(1, (HEIGHT // 10)) * 10]
            
        fruit_spawn = True
        DISPLAY.fill(BLACK)
        
        for pos in snake_body:
            pygame.draw.rect(DISPLAY, GREEN,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(DISPLAY, WHITE, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > WIDTH-10:
            print(f"final score: {score}")
            return

        if snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
            print(f"final score: {score}")
            return

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                print(f"final score: {score}")
                return

        # displaying score countinuously
        show_score(score)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refres Rate
        FPSCLOCK.tick(FPS)


# displaying Score function
def show_score(score):
	score_surface = BASICFONT.render('Score : ' + str(score), True, WHITE)
	score_rect = score_surface.get_rect()
	DISPLAY.blit(score_surface, score_rect)

def gameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WIDTH / 2, 10)
    overRect.midtop = (WIDTH / 2, gameRect.height + 10 + 25)
    

    DISPLAY.blit(gameSurf, gameRect)
    DISPLAY.blit(overSurf, overRect)
    pressKeyScreen()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def startScreen():
    while True:
        DISPLAY.fill(BLACK)
        pressKeyScreen()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def pressKeyScreen():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect = (WIDTH - 200, HEIGHT - 30)
    DISPLAY.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
