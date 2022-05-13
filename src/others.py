import os
import pygame
from pygame import mixer

dirname = os.path.dirname(__file__)
screen = pygame.display.set_mode((750, 650))

def icon():
    """ Retrieves the image file and sets it as an icon.
    """
    pygame.display.set_icon(pygame.image.load(os.path.join(dirname, "objects", "icon.png")))

def music():
    """ Retrieves the music file from the music mixer and sets the mixer volume.
    """
    mixer.music.load(os.path.join(dirname, "sounds","background_music.mp3"))
    pygame.mixer.music.set_volume(0.3)

def sound():
    """ Retrieves the audio file and plays it.
    """
    mixer.Sound.play(mixer.Sound(os.path.join(dirname, "sounds", "pong_sound.wav")))
    