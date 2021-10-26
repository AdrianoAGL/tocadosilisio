import pygame

class Player:
    def __init__(self, player_position_x, player_position_y, player_width, player_height, player_colour):
        self.position_x = player_position_x
        self.position_y = player_position_y
        self.width = player_width
        self.height = player_height
        self.colour = player_colour
        self.rect = (player_position_x, player_position_y, player_width, player_height)
        self.velocity = 5

    def draw(self, window):  # Esta função desenha os personagens dos jogadores (ainda em desenvolvimento).
        pygame.draw.rect(window, self.colour, self.rect)

    def move(self):  # Esta função é responsável pela movimentação dos personagens (provavelmente, ainda será alterada).
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position_y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.position_y += self.velocity
        if keys[pygame.K_LEFT] and self.position_x > 135:
            self.position_x -= self.velocity
        if keys[pygame.K_RIGHT] and self.position_x < 970:
            self.position_x += self.velocity

        self.update()

    def update(self):  # Esta função é responsável por atualizar a posição dos jogadores (ainda em desenvolvimento).
        self.rect = (self.position_x, self.position_y, self.width, self.height)

    def skill(self, screen):  # Esta função será responsável pela ativação das habilidades dos personagens (ainda em desenvolvimento).
        pygame.init()

        colour = (255, 255, 0)
        left = 500
        top = 450
        width = 50
        height = 50
        borde = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            pygame.draw.rect(screen, colour, (left, top, width, height), borde)