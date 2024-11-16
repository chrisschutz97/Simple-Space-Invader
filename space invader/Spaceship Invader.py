import pygame
import random
import math
#https://wall.alphacoders.com/wallpaper.php?i=1008103&w=1920&h=1080&type=crop
#<a target="_blank" href="https://icons8.com/icons/set/laser-beam">Laser Beam icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
#<div>Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

#Intialize pygame
pygame.init()


#Screen
screen = pygame.display.set_mode((1200, 1000))

background = pygame.image.load('space-earth.png')


#Title
pygame.display.set_caption('Predator Killer')
icon = pygame.image.load('icons8-martian-32.png')
pygame.display.set_icon(icon)

#spaceship
spaceshipImg = pygame.image.load('spaceship-60.png')
spaceshipX = 600
spaceshipY = 800
spaceshipX_change = 0
spaceshipY_change = 0


#predator

predatorImg = []
predatorX = []
predatorY = []
predatorX_change = []
predatorY_change = []
num_of_predator = 6

for i in range(num_of_predator):
    predatorImg.append(pygame.image.load('icons8-predator-40.png'))
    predatorX.append(random.randint(0, 1000))
    predatorY.append(random.randint(0, 500))
    predatorX_change.append(5)
    predatorY_change.append(50)
#predator = predato rImg

#laser
laserImg = pygame.image.load('icons8-laser-beam-16.png')
laserX = 0
laserY = 800
laserX_change = 0
laserY_change = 10
laser_state = 'ready'

score = 0

def spaceship(x, y):
    screen.blit(spaceshipImg, (x, y))

def predator(x, y, i):        
    screen.blit(predatorImg[i], (x, y))

def fire_laser(x, y):
    global laser_state
    laser_state = 'fire'
    screen.blit (laserImg, (x, y))

def isCollision(predatorX, predatorY, laserX, laserY):
    distance = math.sqrt((math.pow(predatorX - laserX, 2)) + (math.pow(predatorY - laserY, 2)))
    if distance < 27:
        return True
    else:
        return False


#Game Loop
running = True
while running: 

    screen.fill((25, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                spaceshipY_change = 8
            if event.key == pygame.K_UP:
                spaceshipY_change = -8
            if event.key == pygame.K_LEFT:
                spaceshipX_change = -8
            if event.key == pygame.K_RIGHT:
                spaceshipX_change = 8
            if event.key == pygame.K_SPACE:
                if laser_state is 'ready':
                    laserX = spaceshipX
                    laserY = spaceshipY
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceshipX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                spaceshipY_change = 0
        

    spaceshipX += spaceshipX_change
    spaceshipY += spaceshipY_change

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 1168:
        spaceshipX = 1168
    if spaceshipY <= 0:
        spaceshipY = 0
    elif spaceshipY >= 940:
        spaceshipY = 940

    for i in range (num_of_predator):
        predatorX[i] += predatorX_change[i]

        if predatorX[i] <= 0:
            predatorX_change[i] = 5
            predatorY[i] += predatorY_change[i]
        elif predatorX[i] >= 1168:
            predatorX_change[i] = -5
            predatorY[i] += predatorY_change[i]
            #predatorX[i] = predatorX[i] - predatorX_change
            
        #else:
            #predatorX += 5

        collision = isCollision (predatorX[i], predatorY[i], laserX, laserY)
        if collision: 
            laserY = 800
            laser_state = 'ready'
            score += 1
            print(score)
            predatorX[i] = random.randint(0, 1000)
            predatorY[i] = random.randint(0, 500)

        predator(predatorX[i], predatorY[i], i)

    if laserY <= 0:
        laserY = 800
        laser_state = 'ready'

    if laser_state is 'fire':
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    
        
    #predator(predatorX, predatorY)
    spaceship(spaceshipX, spaceshipY)
    pygame.display.update()


    
