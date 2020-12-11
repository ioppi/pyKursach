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
        self.sound_volume = 0.01
        self.block_size = 120
        self.block_value = 45
        self.time = 60

        try:
            f = open("setting.txt", "r")
            s = f.readline(100)
            self.speed = int(s[s.find(" = ")+3:len(s)])
            s = f.readline(100)
            self.sound_volume = int( s[s.find(" = ") + 3:len(s)])
            s = f.readline(100)
            self.time = int(s[s.find(" = ") + 3:len(s)])
            s = f.readline(100)
            self.block_size = int(s[s.find(" = ") + 3:len(s)])
            s = f.readline(100)
            self.block_value = int(s[s.find(" = ") + 3:len(s)])
            f.close()
        except:
            f = open("setting.txt", "w")
            f.write(f"speed = {self.speed} \n" 
                    f"sound_volume = {self.sound_volume} \n"
                    f"time = {self.time} \n"
                    f"block_size = {self.block_size} \n"
                    f"block_value = {self.block_value} \n")
            f.close()
