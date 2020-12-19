import pygame


class Support:
    def __init__(self):
        self.change_y, self.change_x, self.rect, self.right, self.image, self.speed, self.lvl = None
        # карта уровней для проверуи столкновений

    # все перемещения игрока
    def go_up(self):
        coll = self.collision()
        if coll[0] or coll[1]:
            self.change_y = -self.speed  # Двигаем игрока по y в верх

    def go_down(self):
        coll = self.collision()
        if coll[0] or coll[3]:
            self.change_y = self.speed  # Двигаем игрока по y в низ

    def go_left(self):
        coll = self.collision()
        if coll[0] or coll[4]:
            self.change_x = -self.speed  # Двигаем игрока по Х
        if self.right:  # Проверяем куда он смотрит и если что, то переворачиваем его
            self.flip()
            self.right = False

    def go_right(self):
        # то же самое, но вправо
        coll = self.collision()
        if coll[0] or coll[2]:
            self.change_x = self.speed
        if not self.right:
            self.flip()
            self.right = True

    def collision(self):
        moving = [True, True, True, True, True]
        a = 20

        for block in self.lvl:
            if pygame.sprite.collide_rect(self, block):
                moving[0] = False
            if block.rect.bottom-a < self.rect.top <= block.rect.bottom:
                moving[1] = False
                """if :
                    self.rect.top = block.rect.bottom + 1"""
            if block.rect.left+a > self.rect.right >= block.rect.left:
                moving[2] = False
            if block.rect.top+a > self.rect.bottom >= block.rect.top:
                moving[3] = False
            if block.rect.right-a < self.rect.left <= block.rect.right:
                moving[4] = False
        # print(moving)
        return moving

    def stop(self):
        # вызываем этот метод, когда не нажимаем на клавиши
        self.change_x = 0
        self.change_y = 0

    def flip(self):
        # переворот игрока (зеркальное отражение)
        self.image = pygame.transform.flip(self.image, True, False)
