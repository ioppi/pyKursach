import pygame


class Support:
    def __init__(self):
        self.change_y, self.change_x, self.rect, self.right, self.image, self.speed, self.lvl = None
        # карта уровней для проверуи столкновений

    # все перемещения игрока
    def go_up(self):
        if self.collision():
            self.change_y = -self.speed  # Двигаем игрока по y в верх

    def go_down(self):
        if self.collision():
            self.change_y = self.speed  # Двигаем игрока по y в низ

    def go_left(self):
        if self.collision():
            self.change_x = -self.speed  # Двигаем игрока по Х

        if self.right:  # Проверяем куда он смотрит и если что, то переворачиваем его
            self.flip()
            self.right = False

    def go_right(self):
        # то же самое, но вправо
        if self.collision()[0]:
            self.change_x = self.speed
        if not self.right:
            self.flip()
            self.right = True

    def collision(self):
        moving = [True, True, True, True, True]
        for block in self.lvl:
            if pygame.sprite.collide_rect(self, block):
                moving[0] = False
        return moving

    def stop(self):
        # вызываем этот метод, когда не нажимаем на клавиши
        self.change_x = 0
        self.change_y = 0

    def flip(self):
        # переворот игрока (зеркальное отражение)
        self.image = pygame.transform.flip(self.image, True, False)

