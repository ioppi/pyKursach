import pygame


class Setting:
    def __init__(self):
        pygame.init()
        self.speed = 10
        self.skin = "img/player_cat.png"
        self.infoObject = pygame.display.Info()
        self.width = self.infoObject.current_w
        self.height = self.infoObject.current_h
        self.size_screen = [self.width, self.height]
        self.frames_per_second = 30
        self.sound_volume = 0.1
        self.block_size = 120
        self.block_value = 45
        self.time = 1

        try:
            f = open("setting.txt", "r")
            f.close()
        except FileNotFoundError:
            f = open("setting.txt", "w")
            f.write(f"speed = {self.speed} \n" 
                    f"frames_per_second = {self.frames_per_second} \n"
                    f"sound_volume = {self.sound_volume} \n"
                    f"time = {self.time} \n"
                    f"block_size = {self.block_size} \n"
                    f"block_value = {self.block_value} \n")
            f.close()
