import pygame

def load_music(music):
    pygame.mixer.init()
    track = pygame.mixer.music.load(music)
    pygame.mixer.music.play()
