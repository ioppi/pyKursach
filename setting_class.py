import pygame


class Setting:
    def __init__(self):
        pygame.init()
        self.speed = 10
        self.skin = "img/player_cat.png"
        self.infoObject = pygame.display.Info()
        self.width = self.infoObject.current_w
        self.height = self.infoObject.current_h
        self.size_screen = [self.width,  self.height]
        self.frames_per_second = 30
        self.sound_volume = 0
        self.block_size = 120
        self.time = 90

    def download_setting(self):
        pass

    def save_setting(self):
        pass

