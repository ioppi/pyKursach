import pygame
import support_pl_bt
import random


class Player(pygame.sprite.Sprite, support_pl_bt.Support):
    right = True

    def __init__(self, img_bot_path, speed_bot):
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # картинка, бота
        self.image = pygame.image.load(img_bot_path)
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()

        #  уровень на котором находится игрок
        self.level_bot = random.randint(0, 3)
        # вектор перемещения (для отслеживания столкновений) на будующее
        self.change_x = 0
        self.change_y = 0
        # скорость перемешения
        self.speed = speed_bot
