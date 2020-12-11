from Game_methods import *
import setting_class

mainClock = pygame.time.Clock()
pygame.display.set_caption('HideAndSeek')
screen = pygame.display.set_mode(st.size_screen, 0, 32)
font = pygame.font.SysFont('phosphate', 50)
# класс с настройками
st = setting_class.Setting()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    global click
    while True:
        # вырисовка меню
        screen.fill((25, 25, 112))
        cat_surf = pygame.image.load('../pyKursach/img/1.png')
        cat_rect = cat_surf.get_rect(bottomright=(1000, 700))
        screen.blit(cat_surf, cat_rect)
        draw_text('Главное меню', font, (123, 104, 238), screen, 30, 30)
        # музыка
        pygame.mixer.music.load('../pyKursach/music/The Weeknd - Blinding Lights.mp3')
        pygame.mixer.music.set_volume(st.sound_volume)
        # координаты мышки и расположение кнопок
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(100, 200, 300, 100)
        # появление мышки (появляется розовая рамка) на кнопке и нажатие
        if button_1.collidepoint((mx, my)):
            button_12 = pygame.Rect(90, 190, 320, 120)
            pygame.draw.rect(screen, (221, 160, 221), button_12)
            if click:
                pygame.mixer.music.play()
                run_game()
        # внешний вид кнопок
        pygame.draw.rect(screen, (123, 104, 238), button_1)
        draw_text('играть', font, (0, 0, 0), screen, 160, 220)

        # нажатие на кнопку
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
