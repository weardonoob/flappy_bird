import pygame, pyautogui, time, random, os
pygame.font.init()
pygame.mixer.init()
#mixer is for sounds
WIDTH, HEIGHT = pyautogui.size()
TITLE = "flappy_bird"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
floor = pygame.transform.scale(pygame.image.load("floor_flappy_bird.png"),(WIDTH * 2,HEIGHT / 3))
scroll = 0
scroll_speed = -5
while True:
    screen.fill("black")
    screen.blit(floor,(scroll,HEIGHT * 2 / 3))
    scroll += scroll_speed
    if scroll < -WIDTH / 2:
        scroll = 0

    pygame.display.update()









