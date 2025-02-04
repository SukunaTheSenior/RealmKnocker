import pyglet
from config import *

class SettingsManager:
    def __init__(self, window):
        self.window = window
        self.current_resolution = 0
        self.fullscreen = START_FULLSCREEN
        
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.window.set_fullscreen(self.fullscreen)
        
    def next_resolution(self):
        self.current_resolution = (self.current_resolution + 1) % len(RESOLUTIONS)
        width, height = RESOLUTIONS[self.current_resolution]
        self.window.set_size(width, height)
        
    def get_current_resolution(self):
        return RESOLUTIONS[self.current_resolution]