import pygame, pyautogui, time, random, os
pygame.font.init()
pygame.mixer.init()
#mixer is for sounds
WIDTH, HEIGHT = pyautogui.size()
TITLE = "flappy_bird"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#   floor = pygame.transform.scale(pygame.image.load("floor_flappy_bird.png"),(WIDTH * 2,HEIGHT / 3))
bg = pygame.transform.scale(pygame.image.load("day_sky.png"),(WIDTH *1.5,HEIGHT))
scroll = -WIDTH / 2
scroll_speed = +5

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.images = []
       for i in range(3):
           self.images.append(pygame.image.load(f"bird_fly{i+1}.png"))
       self.index = 0
       self.image = self.images[self.index]
       self.rect = self.image.get_rect()
       self.rect.center = (WIDTH - 100, HEIGHT / 2)
       self.counter = 0
    def update(self):
       self.counter+= 1
       if self.counter >= 6:
          self.counter = 0
          self.index += 1

          if self.index >= 3:
                self.index = 0
       self.image = self.images[self.index]
group1 = pygame.sprite.Group()
bird = Flappy()
group1.add(bird)


while True:
   # screen.fill("black")
    screen.blit(bg,(scroll, 0))
    #screen.blit(floor,(scroll,HEIGHT * 2 / 3))
    scroll += scroll_speed
    if scroll > WIDTH + (WIDTH / 2):
        scroll = 0
    bird.update()
    group1.draw(screen)



    pygame.display.update()









