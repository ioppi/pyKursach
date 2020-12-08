import pygame
import random
import player_class
import bots_class
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
    # начальное расположение игрока
    spawn(player)

    levels_map = Levels()
    bots = []
    for i in range(5):
        b = bots_class.Bot(st.speed+1)
        spawn(b)
        bots.append(b)
    print(bots)
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

    # для отрисовки спрайтов
    pl_sprite_list = pygame.sprite.Group()
    pl_sprite_list.add(player)
    bt_sprite_list = pygame.sprite.Group()
    for b in bots:
        bt_sprite_list.add(b)
    print(bt_sprite_list)
    # уровень на котором мы сейчас находимся (важная переменнаяб бот должен иметь такой параметр)
    # player.level_player
    # Используется для управления скоростью обновления экрана(кадры в секунду)
    clock = pygame.time.Clock()

    n_tick = 0
    game_time = 0
    remaining_time = st.time
    # остновной цикл
    run = True
    game = True
    win = False
    while run:
        n_tick += 1
        if n_tick % 30 == 0:
            game_time += 1
        if game:
            if remaining_time - game_time <= 0:
                game = False
            if player.score == 5:
                game = False
                win = True
            # кадры в секунду
            clock.tick(st.frames_per_second)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
            # метод движения игрока
            move_player(player, levels_map.block_map)
            for i in bots:
                move_bot(i, levels_map.block_map, player, game_time)
            # отрисовка всего и вся
            draw(screen, bg, pl_sprite_list, bt_sprite_list, player.level_id, levels_map, (remaining_time - game_time),
                 player.score)
        else:
            f = pygame.font.Font(None, 200)
            button = pygame.Rect(st.width/2-325, st.height/2-100, 650, 200)
            if win:
                text = f.render("You Win", True, (0, 180, 0))
            else:
                text = f.render("You Lose", True, (180, 0, 0))

            pygame.draw.rect(screen, [0, 0, 180], button)
            screen.blit(text, (st.width/2-305, st.height/2-60))
            pygame.display.update()
            game_time = 0
            remaining_time = 0

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False


# метод отрисовки всего (есои чтото нужно орисовать кидаем это сюда)
def draw(screen, bg, pl, bt, level, block_map, game_time, score):
    # отрисовка заднего фона
    screen.blit(bg[level], (0, 0))
    active_bt = pygame.sprite.Group()
    for i in bt:
        i.update()
        if i.level_id == level:
            active_bt.add(i)
    active_bt.draw(screen)

    block_map.update()
    block_map.draw(level, screen)
    # обновление позиции персонажа
    pl.update(active_bt)
    pl.draw(screen)

    f = pygame.font.Font(None, 30)
    button = pygame.Rect(st.width / 2 - 20, 0, 40, 20)
    text = f.render(f"{game_time}", True, (0, 180, 0))
    pygame.draw.rect(screen, [0, 0, 180], button)
    screen.blit(text, (st.width / 2 - 10, 2))
    f = pygame.font.Font(None, 40)
    text = f.render(f"{score}/5", True, (200, 0, 0))
    screen.blit(text, (st.width/2 + 35, 2))
    # обновление экрана
    pygame.display.update()


# метод движение персонажа
def move_player(player, level_maps):
    # останавливаем движение, если кнопки движения нажаты продолжает двигаться
    player.stop()
    player.lvl = level_maps[player.level_id]
    # нажатые кнопки
    keys = pygame.key.get_pressed()
    # движение
    if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        if keys[pygame.K_UP]:
            move_up(player)
        if keys[pygame.K_DOWN]:
            move_down(player)
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            player.change_y = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        if keys[pygame.K_LEFT]:
            move_left(player)
        if keys[pygame.K_RIGHT]:
            move_right(player)
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            player.change_x = 0


# метод движение ботов
def move_bot(bot, level_maps, pl, t):  # 0-up/1-right/2-down/3-left/
    bot.lvl = level_maps[bot.level_id]
    bot.stop()
    if bot.bot_live:
        mv = bot.get_move(pl, t)
        if mv[0] == 0:
            move_up(bot)
        if mv[0] == 2:
            move_down(bot)
        if mv[1] == 1:
            move_right(bot)
        if mv[1] == 3:
            move_left(bot)


# вспомогательные методы для двмжения бота и игрока
# вверх
def move_up(pl_bt):
    if (pl_bt.level_id == 0 or pl_bt.level_id == 1) and pl_bt.rect.y >= 2:
        pl_bt.go_up()
    elif pl_bt.level_id == 2 or pl_bt.level_id == 3:
        if pl_bt.rect.y <= -10:
            pl_bt.rect.y = st.height - 80
            if pl_bt.level_id == 2:
                pl_bt.level_id = 0
            elif pl_bt.level_id == 3:
                pl_bt.level_id = 1
        pl_bt.go_up()


# вниз
def move_down(pl_bt):
    if (pl_bt.level_id == 2 or pl_bt.level_id == 3) and pl_bt.rect.y <= st.height - 60:
        pl_bt.go_down()
    elif pl_bt.level_id == 0 or pl_bt.level_id == 1:
        if pl_bt.rect.y >= st.height - 30:
            pl_bt.rect.y = -5
            if pl_bt.level_id == 0:
                pl_bt.level_id = 2
            elif pl_bt.level_id == 1:
                pl_bt.level_id = 3
        pl_bt.go_down()


# влево
def move_left(pl_bt):
    if (pl_bt.level_id == 0 or pl_bt.level_id == 2) and pl_bt.rect.x >= 2:
        pl_bt.go_left()
    elif pl_bt.level_id == 1 or pl_bt.level_id == 3:
        if pl_bt.rect.x <= -10:
            pl_bt.rect.x = st.width - 70
            if pl_bt.level_id == 1:
                pl_bt.level_id = 0
            elif pl_bt.level_id == 3:
                pl_bt.level_id = 2
        pl_bt.go_left()


# вправо
def move_right(pl_bt):
    if (pl_bt.level_id == 1 or pl_bt.level_id == 3) and pl_bt.rect.x <= st.width - 60:
        pl_bt.go_right()
    elif pl_bt.level_id == 0 or pl_bt.level_id == 2:
        if pl_bt.rect.x >= st.width - 30:
            pl_bt.rect.x = -10
            if pl_bt.level_id == 0:
                pl_bt.level_id = 1
            elif pl_bt.level_id == 2:
                pl_bt.level_id = 3
        pl_bt.go_right()


def spawn(pl_bt):
    if random.choice([True, False]):
        x = random.randint(0, st.width-50)
        if random.choice([True, False]):
            y = random.randint(0, (st.block_size-51))
        else:
            y = random.randint((st.height-st.block_size), st.height-51)
    else:
        y = random.randint(0, st.height - 51)
        if random.choice([True, False]):
            x = random.randint(0, (st.block_size - 51))
        else:
            x = random.randint((st.width - st.block_size), st.width - 51)

    pl_bt.rect.x = x
    pl_bt.rect.y = y
