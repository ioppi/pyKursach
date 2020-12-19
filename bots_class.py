import pygame
import support_pl_bt
import random
import math


class Bot(pygame.sprite.Sprite, support_pl_bt.Support):
    right = True

    def __init__(self, speed_bot):
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # картинка, бота
        self.image = pygame.transform.scale(pygame.image.load("img/mouse.png"), (50, 50))
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()

        #  уровень на котором находится бот
        self.level_id = random.randint(0, 3)
        # вектор перемещения (для отслеживания столкновений) на будующее
        self.change_x = 0
        self.change_y = 0
        # скорость перемешения
        self.speed = speed_bot
        self.bot_live = True

    def get_move(self, pl, t):
        key = [random.choice([0, 2]), random.choice([1, 3])]
        if pl.level_id == self.level_id:
            if math.sqrt((pl.rect.x - self.rect.x) ** 2 + (pl.rect.y - self.rect.y) ** 2) < 600:
                if pl.rect.x < self.rect.x:
                    key[1] = 1
                else:
                    key[1] = 3
                if pl.rect.y > self.rect.y:
                    key[0] = 0
                else:
                    key[0] = 2
            else:
                if self.timer(t):
                    key = [random.choice([0, 2]), random.choice([1, 3])]
        if self.timer(t):
            key = [random.choice([0, 2]), random.choice([1, 3])]
        return key

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if not self.bot_live:
            self.dead()

    def timer(self, t):
        if t % 5 == 0:
            return True
        return False

    def dead(self):
        self.image = pygame.transform.scale(pygame.image.load("img/dead.png"), (40, 40))
