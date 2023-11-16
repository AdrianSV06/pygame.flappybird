import pygame
import sys
import random

pygame.init()

width, height = 800, 600

blue = (0, 180, 255)
yellow = (255, 255, 0)
green = (255, 0, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

class Bird:
    def __init__(self):
        self.size = 50
        self.x = width // 3 - self.size // 2
        self.y = 2
        self.accel = 0
        self.framesflapped = 0
        self.isflapped = False 

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


    def update(self):
        self.y -= self.accel 
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


    def draw(self):
        pygame.draw.rect(screen, yellow, (self.x, self.y, self.size, self.size))
        
    def flap(self):
        if self.isflapped:
            self.framesflapped += 1
            self.accel -= 0.8
            if self.framesflapped == 12: 
                self.framesflapped = 0
                self.isflapped = False
                self.accel = 0

        else:
            if self.accel > -15:
                self.accel -= 1
            

    def collision(self,pipe):
        if self.y > 900 - self.size or self.y < -50 :
            quit()
        if self.rect.colliderect(pipe.Piperect) or self.rect.colliderect(pipe.secondpiperect):
            quit()

class Pipe:
    def __init__(self, x):
        self.size1 = 100
        self.size2 = 1000

    
        self.x = x
        self.y = (random.randint(-50, 400))
        self.speed = 5
        self.secondpipe()

        self.Piperect = pygame.Rect(self.x, self.y, self.size1, self.size2)

    def movepipe(self):
        self.x  -= self.speed
        self.secondpipe_x -= self.speed

        if self.x < -300:
            self.x = 900
            self.y = (random.randint(-50, 400))
            self.secondpipe_x = 900
            self.secondpipe_y = self.y + 200


 

        self.Piperect = pygame.Rect(self.x, 0, self.size1, self.y)
        self.secondpiperect = pygame.Rect(self.secondpipe_x, self.secondpipe_y, self.secondpipe_size1, self.secondpipe_size2)

    
    
    
    def secondpipe(self):
        self.secondpipe_size1 = 100
        self.secondpipe_size2 = 1000
        self.secondpipe_x = self.x
        self.secondpipe_y = self.y + 200
        
        self.secondpiperect = pygame.Rect(self.secondpipe_x, self.secondpipe_y, self.secondpipe_size1, self.secondpipe_size2)

    def draw(self): 
        pygame.draw.rect(screen, green, self.Piperect)
        pygame.draw.rect(screen, green, self.secondpiperect)

       

#pipe = Pipe()

score = 0

bird = Bird()

allpipes = [Pipe(600), Pipe(1200)]

font = pygame.font.SysFont("Calibri", 60, True)
# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.isflapped = True
                bird.framesflapped = 0
                bird.accel = 12
            break

    bird.update()
    bird.flap()
    screen.fill(blue)
    bird.draw()

    for pipe in allpipes:
        pipe.draw()
        pipe.movepipe()
        bird.collision(pipe)
        if 240  == pipe.x:
            score += 1
            print(score)

    scoreText = font.render(str(score), True, (0,0,0))
    screen.blit(scoreText, (5, 5))
  
    pygame.display.flip()
    clock.tick(60)  # 60 FPSS
