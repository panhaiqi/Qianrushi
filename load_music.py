import pygame
import os
def load_music(music,synthesis):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    # pygame.mixer.music.load(synthesis)
    # pygame.mixer.music.play()
    os.system(synthesis)



# def load_music(music,synthesis):
#     os.system(music)
