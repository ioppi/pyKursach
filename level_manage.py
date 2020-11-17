import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, size_block, coords, id_block):
        # Конструктор
        super().__init__()
        # Также указываем фото блока
        self.image = pygame.transform.scale(pygame.image.load(f'img/block_{id_block}.png'), size_block)
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]


def generate(id_generate):
    bl = Block((200, 100), (300, 500), 0)

    group = pygame.sprite.Group()
    group.add(bl)
    return group


class Levels:
    def __init__(self):
        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.level_1 = generate(0)
        self.level_2 = generate(0)
        self.level_3 = generate(0)
        self.level_4 = generate(0)
        self.block_map = [self.level_1, self.level_2, self.level_3, self.level_4]

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self):
        self.level_1.update()

    # Метод для рисования объектов на сцене
    def draw(self, id_level, screen):
        # Рисуем все платформы из группы спрайтов
        if id_level == 0:
            self.level_1.draw(screen)
        elif id_level == 1:
            self.level_1.draw(screen)
        elif id_level == 2:
            self.level_1.draw(screen)
        elif id_level == 3:
            self.level_1.draw(screen)
