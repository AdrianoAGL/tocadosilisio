import pygame
from pygame.locals import *
from Network import Network

# Definindo Constantes de Core==========================================================================================

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Definindo Constantes de Dimensão======================================================================================

window_width = 1080
window_height = 720

champions_board_width = 450
champions_board_height = 360

client_button_width = 120
client_button_height = 60

# Definindo Constantes de Posição=======================================================================================

champions_board_left = 315
champions_board_top = 140

client_button_left = 355
client_button_top = 540

# Inicializando o Pygame================================================================================================

pygame.init()

# Criando Janela do Client==============================================================================================

window_size = (window_width, window_height)  # Define o tamanho da janela do jogo.
inicial_image = 'assets/APERTEESPAÇO.png'
background_image = pygame.image.load(inicial_image)  # Carrega a imagem de fundo da tela inicial.
background_image = pygame.transform.scale(background_image, window_size)  # Deixa a imagem de fundo do tamanho de janela.
clock = pygame.time.Clock()  # Limitador de fps
screen = pygame.display.set_mode(window_size)  # Define o tamanho da janela.
pygame.display.set_caption("Toca do Silício (Fase de Desenvolvimento)")  # Põe um nome na janela.

# Trabalhando as Sprites dos Personagens================================================================================

sprite1 = pygame.image.load('assets/warrior.gif')
sprite1 = pygame.transform.scale(sprite1, (200, 200))
sprite2 = pygame.image.load('assets/arqueiro.gif')
sprite2 = pygame.transform.scale(sprite2, (400, 400))
sprite3 = pygame.image.load('assets/lancer.gif')
sprite3 = pygame.transform.scale(sprite3, (400, 400))
sprite4 = pygame.image.load('assets/maga.gif')
sprite4 = pygame.transform.scale(sprite4, (450, 450))

champion_link = ''

# Definindo Funções=====================================================================================================


def draw_button(position, colour, left, top, width, height, borde):  # Desenha botões.
    pygame.draw.rect(position, colour, (left, top, width, height), borde)


def redraw_screen(screen, map, player1, player2):  # Atualiza a tela redesennhando-a.
    screen.blit(map, (0, 0))

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.update()


def run_game():  # Roda o jogo.
    run = True
    clock.tick(90)
    network = Network()
    player1 = network.get_position()

    while run:
        map = pygame.image.load('assets/mapfinal.png')
        map = pygame.transform.scale(map, window_size)
        screen.blit(map, (0, 0))

        player2 = network.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redraw_screen(screen, map, player1, player2)


# Inicializando o Client================================================================================================

while True:

    for event in pygame.event.get():  # Comandos do jogo.
        if event.type == QUIT:
            screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x >= 153 and x <= 268 and y >= 177 and y <= 293:
                champion_link = 'assets/soldier_sprites/'
                print(champion_link)
            elif x >= 804 and x <= 910 and y >= 191 and y <= 294:
                champion_link = 'assets/arrow_sprites/'
                print(champion_link)
            elif x >= 149 and x <= 241 and y >= 467 and y <= 634:
                champion_link = 'assets/lancer_sprites/'
                print(champion_link)
            elif x >= 806 and x <= 896 and y >= 481 and y <= 638:
                champion_link = 'assets/wicher_sprites/'
                print(champion_link)



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen = False
            if event.key == pygame.K_SPACE:  # Passa da tela inicial para o game ao ser pressionada a tecla SPACE.
                run_game()


    screen.blit(background_image, (0, 0))
    screen.blit(sprite1, (115, 120))
    screen.blit(sprite2, (661, 20))
    screen.blit(sprite3, (1, 350))
    screen.blit(sprite4, (630, 320))
    pygame.display.update()
