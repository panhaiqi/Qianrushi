import pygame

import os
def load_music(music,synthesis):
    # song = pygame.mixer.Sound(music)
    #
    # while True:
    #     song.play()
    pygame.mixer.init()
    #channel1 = pygame.mixer.find_channel()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    # pygame.mixer.music.load(synthesis)
    # pygame.mixer.music.play()
    song = pygame.mixer.Sound(synthesis)
    song.play()
    #os.system(synthesis)



# def load_music(music,synthesis):
#     os.system(music)
