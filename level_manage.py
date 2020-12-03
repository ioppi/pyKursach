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
    grid_blocks = [st.width // block_size, st.height // block_size]
    # делаем сетку и по сетку проверяем правила
    grid = []
    for k in range(0, grid_blocks[1]):
        s = []
        for r in range(0, grid_blocks[0]):
            s.append(False)
        grid.append(s)
    i = st.block_value
    while i > 0:
        bl = Block((block_size, block_size))
        x = random.randrange(1, grid_blocks[0] - 1)
        y = random.randrange(1, grid_blocks[1] - 1)
        if not grid[y][x] and \
                (
                        not (grid[y][x + 1] and grid[y + 1][x] and grid[y + 1][x + 1]) and
                        not (grid[y][x - 1] and grid[y - 1][x] and grid[y - 1][x - 1]) and
                        not (grid[y][x + 1] and grid[y - 1][x] and grid[y - 1][x + 1]) and
                        not (grid[y][x - 1] and grid[y + 1][x] and grid[y + 1][x - 1])
                ):

            if (2 < x < grid_blocks[0] - 2) and (2 < y < grid_blocks[1] - 2):
                if (
                        (not (grid[y][x + 2] and grid[y + 1][x + 1] and grid[y - 1][x + 1])) and
                        (not (grid[y][x - 2] and grid[y + 1][x - 1] and grid[y - 1][x - 1])) and
                        (not (grid[y + 2][x] and grid[y + 1][x + 1] and grid[y + 1][x - 1])) and
                        (not (grid[y - 2][x] and grid[y - 1][x + 1] and grid[y - 1][x - 1]))
                ):
                    bl.rect.x = x * block_size
                    bl.rect.y = y * block_size
                    group.add(bl)
                    grid[y][x] = True
                    i -= 1
            else:
                bl.rect.x = x * block_size
                bl.rect.y = y * block_size
                group.add(bl)
                grid[y][x] = True
                i -= 1

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
