#import library
import pygame, sys, random, math
#initialize pygame
pygame.init()
#screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#title and icon
pygame.display.set_caption("SPACE INVADERS") #set caption
#icon = pygame.image.load("icon.png") #load the image
#player
playerX = 375
playerY = 500
player = pygame.image.load("spaceship.png")
player = pygame.transform.scale(player, (64,64))
#bullet
bulletX = playerX + 15
bulletY = playerY - 35
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet, (32,32))
bulletY_change = -10
#bullet state
#ready (not firing)
#fire  (firing)
bullet_state = 'ready'

#collision
def is_collision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
  if distance <27:
    return True
  else:
    return False
#score
score = 0
scoreX = 10
scoreY = 550
font = pygame.font.Font('freesansbold.ttf',32)

#game over text
over_font= pygame.font.Font('freesansbold.ttf', 64)

#enemy
enemy_number = 5
enemyX = []
enemyY = []
enemy = []
enemyX_change = []
enemyY_change = []
for i in range (enemy_number):
  enemyX.append(random.randint(1,500))
  enemyY.append(random.randint(0,100))
  enemy_single_image = pygame.image.load("enemy.png")
  enemy_single_image = pygame.transform.scale(enemy_single_image, (64,64))
  enemy.append(enemy_single_image)
  enemyX_change.append (30)
  enemyY_change.append (30)

pygame.display.set_icon(icon) # set icon 
#background sounds
mixer.music.load('background.wav')
mixer.music.play(-1)



while True:
    for event in pygame.event.get():
        # When user clicks on the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #player movement
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
      playerY -= 2
    if key_pressed[pygame.K_DOWN]:
      playerY += 2
    if key_pressed[pygame.K_LEFT]:
      playerX -= 2
    if key_pressed[pygame.K_RIGHT]:
      playerX += 2
    #boundaries
    if playerY <= 0:
      playerY = 0
    if playerY >= 536:
      playerY = 536
    if playerX <= 0:
      playerX = 0
    if playerX >= 736:
      playerX = 736
   #boundaries
    for i in range(enemy_number):
      if enemyX[i] <= 0:
        enemyX[i] = 0
        enemyX[i] = 0
        enemyX_change[i] = 3
        enemyY[i] += enemyY_change[i]
      if enemyX[i] >= 736:
        enemyX[i] = 736
        enemyX_change[i] = -3
        enemyY[i] += enemyY_change[i]
      enemyX[i] += enemyX_change[i]
    #background color
    screen.fill((0,0,0  ))
    screen.blit(player, (playerX, playerY))
    for i in range(enemy_number):
      screen.blit(enemy[i], (enemyX[i], enemyY[i]))
    #firing
    if key_pressed[pygame.K_SPACE]:
     if bullet_state == 'ready':
        bullet_state = 'fire'
        bulletX = playerX + 15
        bulletY = playerY - 35
        bulletY += bulletY_change
    if bullet_state == 'fire':
      screen.blit(bullet, (bulletX, bulletY))
      bulletY += bulletY_change
    if bulletY <= 0:
      bullet_state = 'ready'

     #collision detection
    for i in range (enemy_number):
      if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
        bullet_state = 'ready'
        enemyX[i] = random.randint(1,500)
        enemyY[i] = (0)
        score += 1
     #draw score
    score_value = font.render("score:" + str(score),True,(255, 255, 255))
    screen.blit(score_value,(scoreX,scoreY))
    if bullet_state == "ready":
      bulletX = 1000
      bulletY = 1000

    for i in range(enemy_number):
        if enemyY[i] >= 580 or is_collision(enemyX[i], enemyY[i], playerX, playerY):
            over_text = over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(over_text, (200, 250))
            for j in range(enemy_number):
                enemyY[j] = 2000
     #update screen
    pygame.display.update()
