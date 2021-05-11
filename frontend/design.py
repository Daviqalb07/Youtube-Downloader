import pygame
from urllib import request
from PIL import Image

# Imprime texto no display (screen)
def print_text(texto: str, screen: pygame.Surface, fonte: pygame.font.Font, pos: list, cor: tuple):
    text_surface = fonte.render(texto, True, cor)
    screen.blit(text_surface, pos)

# Imprime o título completo
## Difere do print_text() caso tamanho do título do vídeo seja maior que a largura da janela
def print_just_title(text: str, screen: pygame.Surface, fonte: pygame.font.Font, pos: list, cor: tuple):
    pos_print = [pos[0], pos[1]]
    length = len(text)

    inicio = 0
    enter = 60
    while inicio <= length:
        end = min(enter, length)
        print_text(text[inicio:end], screen, fonte, pos_print, cor)

        pos_print[1] = pos_print[1] + 17      
        inicio = inicio + 61
        enter = enter + 60


# Mostra a thumbnail do vídeo.
def show_thumbnail(screen: pygame.Surface, url: str):
    img_PIL = Image.open(request.urlopen(url))
    img_size = 240, 160
    img_PIL.thumbnail(img_size, Image.ANTIALIAS)
    img = pygame.image.fromstring(img_PIL.tobytes(), img_PIL.size, img_PIL.mode).convert()
    screen.blit(img, (155, 35))

# Configurando template do botão
class Button:
    def __init__(self, button_config: tuple):
        self.rect = pygame.Rect(button_config)

    # Define a cor do botão.
    def set_color(self, color_button: tuple):
        self.color = color_button

    # Retorna as coordenadas do centro do botão.
    def get_center(self):
        return self.rect.center

    # Retorna:
    ## True, se as coordenadas pertencem ao botão.
    ## False, caso contrário.
    def get_collide(self, coord: tuple):
        return self.rect.collidepoint(coord)
    
    # Desenha o botão
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)





# Configurando template da caixa de texto
class Input_Box:
    def __init__(self, box_config: tuple):
        self.box = pygame.Rect(box_config)
        self.active = False

    def set_color(self, color: tuple):
        self.color = color

    # Ativa/desativa a caixa de entrada.
    def set_active(self, status: bool):
        self.active = status
    
    # Retorna:
    ## True, se a caixa de entrada está ativa.
    ## False, caso contrário.
    def get_active(self):
        return self.active
    
    # Retorna:
    ## True, se as coordenadas pertencem à caixa de entrada.
    ## False, caso contrário.
    def get_collide(self, coord: tuple):
        return self.box.collidepoint(coord)

    # Retorna coordenada X do canto superior esquerdo da caixa.
    def get_box_x(self):
        return self.box.x

    # Retorna coordenada Y do canto superior esquerdo da caixa.
    def get_box_y(self):
        return self.box.y

    # Desenha a caixa de entrada.
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.box)
