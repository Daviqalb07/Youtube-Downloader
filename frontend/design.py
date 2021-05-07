import pygame

def print_text(texto: str, screen: pygame.Surface, fonte: pygame.font.Font, pos: tuple, cor: tuple):
    text_surface = fonte.render(texto, True, cor)
    screen.blit(text_surface, pos)

# Configurando template do botão
class Button:
    def __init__(self, button_config: tuple):
        self.rect = pygame.Rect(button_config)

    def set_color(self, color_button: tuple):
        self.color = color_button

    def get_center(self):
        return self.rect.center

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)

# Configurando template da caixa de texto
class Input_Box:
    def __init__(self, box_config: tuple):
        self.box = pygame.Rect(box_config)
        self.active = False

    def set_color(self, color: tuple):
        self.color = color

    def set_active(self, status: bool):
        self.active = status
    
    def get_active(self):
        return self.active

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.box)
