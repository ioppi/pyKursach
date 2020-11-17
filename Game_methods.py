import pygame
import player_class
from level_manage import Levels
import setting_class
import sys
from pygame.locals import *

# инициализация
pygame.init()
# класс с настройками
st = setting_class.Setting()


# основной метод игры
def run_game():
    # создание игрока
    player = player_class.Player(st.skin, st.speed)
    levels_map = Levels()
    # инициализация и размер экрана
    screen = pygame.display.set_mode(st.size_screen)
    # название окна (игры)
    pygame.display.set_caption("HideAndSeek")
    # задний фон
    bg = [pygame.image.load("../pyKursach/img/bg_home.jpg"), pygame.image.load("../pyKursach/img/bg_forest.jpg"),
          pygame.image.load("../pyKursach/img/bg_dungeon.jpg"), pygame.image.load("../pyKursach/img/bg_sky.jpg")]
    #  заднего фона под экран
    for i in range(4):
        bg[i] = pygame.transform.scale(bg[i], st.size_screen)
    # Используется для управления скоростью обновления экрана(кадры в секунду)
    clock = pygame.time.Clock()
    # отрисовка спрайтов
    active_sprite_list = pygame.sprite.Group()
    # начальное расположение игрока
    player.rect.x = 250
    player.rect.y = 250
    active_sprite_list.add(player)

    # уровень на котором мы сейчас находимся (важная переменнаяб бот должен иметь такой параметр)
    # player.level_player

    # остновной цикл
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        # метод движения игрока + скролинг заднего фона и препятствий в будующем
        move_player(player, levels_map.block_map, player.level_player)
        # отрисовка всего и вся
        draw(screen, bg, active_sprite_list, player.level_player, levels_map)
        # кадры в секунду
        clock.tick(st.frames_per_second)


# метод движение персонажа
def move_player(player, level_maps, level_id):
    # останавливаем движение, если кнопки движения нажаты продолжает двигаться
    player.stop()
    permission_move = collision(player, level_maps, level_id)
    # нажатые кнопки
    keys = pygame.key.get_pressed()
    # движение
    if not permission_move[0]:
        if keys[pygame.K_UP]:
            move_up(player)
        if keys[pygame.K_DOWN]:
            move_down(player)
        if keys[pygame.K_LEFT]:
            move_left(player)
        if keys[pygame.K_RIGHT]:
            move_right(player)
    else:
        if keys[pygame.K_UP] and permission_move[1]:
            move_up(player)
        if keys[pygame.K_DOWN] and permission_move[2]:
            move_down(player)
        if keys[pygame.K_LEFT] and permission_move[3]:
            move_left(player)
        if keys[pygame.K_RIGHT] and permission_move[4]:
            move_right(player)


# метод движение ботов
def move_bot(bot, key):  # 0-up/1-down/2-left/3-right
    bot.stop()
    if key == 0:
        move_up(bot)
    if key == 1:
        move_down(bot)
    if key == 2:
        move_left(bot)
    if key == 3:
        move_right(bot)


# вспомогательные методы для двмжения бота и игрока
# вверх
def move_up(pl_bt):
    if (pl_bt.level_player == 0 or pl_bt.level_player == 1) and pl_bt.rect.y >= 2:
        pl_bt.go_up()
    elif pl_bt.level_player == 2 or pl_bt.level_player == 3:
        if pl_bt.rect.y <= -10:
            pl_bt.rect.y = st.height - 80
            if pl_bt.level_player == 2:
                pl_bt.level_player = 0
            elif pl_bt.level_player == 3:
                pl_bt.level_player = 1
        pl_bt.go_up()


# вниз
def move_down(pl_bt):
    if (pl_bt.level_player == 2 or pl_bt.level_player == 3) and pl_bt.rect.y <= st.height - 100:
        pl_bt.go_down()
    elif pl_bt.level_player == 0 or pl_bt.level_player == 1:
        if pl_bt.rect.y >= st.height - 90:
            pl_bt.rect.y = -5
            if pl_bt.level_player == 0:
                pl_bt.level_player = 2
            elif pl_bt.level_player == 1:
                pl_bt.level_player = 3
        pl_bt.go_down()


# влево
def move_left(pl_bt):
    if (pl_bt.level_player == 0 or pl_bt.level_player == 2) and pl_bt.rect.x >= 2:
        pl_bt.go_left()
    elif pl_bt.level_player == 1 or pl_bt.level_player == 3:
        if pl_bt.rect.x <= -10:
            pl_bt.rect.x = st.width - 70
            if pl_bt.level_player == 1:
                pl_bt.level_player = 0
            elif pl_bt.level_player == 3:
                pl_bt.level_player = 2
        pl_bt.go_left()


# вправо
def move_right(pl_bt):
    if (pl_bt.level_player == 1 or pl_bt.level_player == 3) and pl_bt.rect.x <= st.width - 80:
        pl_bt.go_right()
    elif pl_bt.level_player == 0 or pl_bt.level_player == 2:
        if pl_bt.rect.x >= st.width - 70:
            pl_bt.rect.x = -10
            if pl_bt.level_player == 0:
                pl_bt.level_player = 1
            elif pl_bt.level_player == 2:
                pl_bt.level_player = 3
        pl_bt.go_right()


def collision(pl_bt, level_maps, level_id):
    # Следим ударяем ли мы какой-то другой объект
    sprite_list = level_maps[level_id]
    # Перебираем все возможные объекты, с которыми можем столкнуться
    for sprite in sprite_list:
        if pl_bt.rect.right > sprite.rect.left and pl_bt.rect.left < sprite.rect.right and \
                pl_bt.rect.top < sprite.rect.bottom and pl_bt.rect.bottom > sprite.rect.top:
            col = True
        else:
            col = False
        if sprite.rect.bottom-20 < pl_bt.rect.top < sprite.rect.bottom:
            top = False
        else:
            top = True
        if sprite.rect.top+20 > pl_bt.rect.bottom > sprite.rect.top:
            bottom = False
        else:
            bottom = True
        if sprite.rect.right-20 < pl_bt.rect.left < sprite.rect.right:
            left = False
        else:
            left = True
        if sprite.rect.left+20 > pl_bt.rect.right > sprite.rect.left:
            right = False
        else:
            right = True

        return [col, top, bottom, left, right]


# метод отрисовки всего (есои чтото нужно орисовать кидаем это сюда)
def draw(screen, bg, active_sprite_list, level, block_map):
    # отрисовка заднего фона
    screen.blit(bg[level], (0, 0))
    block_map.update()
    block_map.draw(level, screen)
    # обновление позиции персонажа
    active_sprite_list.update()
    active_sprite_list.draw(screen)
    # обновление экрана
    pygame.display.update()
