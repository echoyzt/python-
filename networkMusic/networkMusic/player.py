from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from io import BytesIO

class Player:
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.music

    def reset(self):
        self.music.stop()
        pygame.mixer.pre_init()

    def load(self, filename):
        self.music.load(filename)

    def play(self):
        self.music.play(loops=-1)

    def pause(self):
        self.music.pause()

    def unpause(self):
        self.music.unpause()

    def stop(self):
        self.music.stop()

    def get_length(self):
        return self.music.get_length()

    def get_pos(self):
        return self.music.get_pos()

    def set_pos(self, value=0):
        self.music.rewind()
        self.music.set_pos(value)

    def get_volume(self):
        return self.music.get_volume()

    def set_volume(self, value=0.5):
        return self.music.get_volume(value)

    def addsong(self, filename):
        self.music.quene(filename)