import pygame
from support_pl_bt import Support
import random


class Player(pygame.sprite.Sprite, Support):
    # Изначально игрок смотрит вправо, поэтому эта переменная True
    right = True

    def __init__(self, img_player_path, speed_player):
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # картинка игрока
        self.image = pygame.transform.scale(pygame.image.load(img_player_path), (50, 50))
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()
        #  уровень на котором находится игрок
        self.level_id = random.randint(0, 3)
        # вектор перемещения (для отслеживания столкновений) на будующее
        self.change_x = 0
        self.change_y = 0
        # скорость перемешения
        self.speed = speed_player

    def update(self):
        # Передвигаем его
        # change_x/y будет меняться при нажатии на стрелочки клавиатуры
        self.rect.x += self.change_x
        self.rect.y += self.change_y
