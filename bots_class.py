import pygame
import support_pl_bt
import random


class Bot(pygame.sprite.Sprite, support_pl_bt.Support):
    right = True

    def __init__(self, speed_bot):
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # картинка, бота
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()

        #  уровень на котором находится бот
        self.level = random.randint(0, 3)
        # вектор перемещения (для отслеживания столкновений) на будующее
        self.change_x = 0
        self.change_y = 0
        # скорость перемешения
        self.speed = speed_bot

