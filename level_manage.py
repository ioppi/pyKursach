import pygame
import random
import setting_class


class Block(pygame.sprite.Sprite):
    def __init__(self, size_block):
        # Конструктор
        super().__init__()
        # Также указываем фото блока
        self.image = pygame.Surface(size_block)
        self.image.fill((0, 0, 0))
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()


def generate():
    st = setting_class.Setting()
    group = pygame.sprite.Group()
    block_size = st.block_size
    grid_blocks = [st.width//block_size, st.height//block_size]
    for i in range(50):
        bl = Block((block_size,  block_size))
        bl.rect.x = random.randrange(1, grid_blocks[0]-1)*block_size
        bl.rect.y = random.randrange(1, grid_blocks[1]-1)*block_size
        group.add(bl)
    return group


class Levels:
    def __init__(self):
        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.level_1 = pygame.sprite.Sprite
        self.level_2 = pygame.sprite.Sprite
        self.level_3 = pygame.sprite.Sprite
        self.level_4 = pygame.sprite.Sprite
        self.level_1 = generate()
        self.level_2 = generate()
        self.level_3 = generate()
        self.level_4 = generate()
        self.block_map = [self.level_1, self.level_2, self.level_3, self.level_4]

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self):
        self.level_1.update()
        self.level_2.update()
        self.level_3.update()
        self.level_4.update()

    # Метод для рисования объектов на сцене
    def draw(self, id_level, screen):
        # Рисуем все платформы из группы спрайтов
        if id_level == 0:
            self.level_1.draw(screen)
        elif id_level == 1:
            self.level_2.draw(screen)
        elif id_level == 2:
            self.level_3.draw(screen)
        elif id_level == 3:
            self.level_4.draw(screen)
