import sys, pygame, os

pygame.init()

size = width, height = 320, 240

speed = [2,0]
xPos = [0,0]
black = 0,0,0

screen = pygame.display.set_mode(size)
path = __file__.replace("sprite walking.py","player/")

step = 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballFile = path + "Run ({0}).png".format(step)
    if step == 8:
        step=1
    else:
        step = step + 1

    ball = pygame.image.load( ballFile).convert()
    ball = pygame.transform.scale(ball,[95,80])
    ballrect = ball.get_rect()
    ballrect.bottom = 240

    xPos[0] = xPos[0] + speed[0]
    xPos[1] = xPos[1] + speed[1]

    ballrect = ballrect.move(xPos)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.delay(100)
