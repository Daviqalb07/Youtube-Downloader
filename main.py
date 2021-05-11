import pygame
import pyperclip
from backend.logic import *
from frontend.design import *

window_size = (550, 420)
display = pygame.display.set_mode(window_size)
pyperclip.init_osx_pbcopy_clipboard()

if __name__ == "__main__":
    pygame.init()
    pygame.scrap.init()

    # Definindo as cores utilizadas (sistema RGB)
    COLOR_RED = (196, 48, 43) # Cor vermelha da logomarca do YouTube
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (173, 173, 173)
    COLOR_BLACK = (0, 0, 0)


    # Configurando título e background da janela.
    pygame.display.set_caption("YouTube Downloader")
    display.fill(COLOR_RED)


    # Construindo o botão de download.
    download = Button((100, 300, 150, 50))    
    download.set_color(COLOR_WHITE)

    # Botão para apagar a entrada de texto.
    clear_input = Button((300, 300, 150, 50))
    clear_input.set_color(COLOR_WHITE)

    # Criando a caixa de entrada de texto.
    box = Input_Box((20, 250, 510, 30))
    box.set_color(COLOR_WHITE)

    # Fonte do texto
    font = pygame.font.Font(None, 30)
    input_url = ""

    info_font = pygame.font.Font(None, 25)
    output_url = ""

    run = True
    while run:

        # Desenhando a caixa de entrada de texto.
        box.draw(display)
        start_text_point = [box.get_box_x() + 5, box.get_box_y() + 5]
        if len(input_url):
            output_url = input_url
        else:
            output_url = "Digite a URL do vídeo"

        print_text(texto = output_url, screen = display, fonte = info_font, pos = start_text_point, cor = COLOR_BLACK)


        # Desenhando o botão download e clear junto com os respectivos textos.
        download.draw(display)
        center_download = download.get_center()
        center_download = [center_download[0] - 47, center_download[1] - 10]
        print_text(texto = "Download", screen = display, fonte = font, pos = center_download, cor = COLOR_BLACK)

        clear_input.draw(display)
        center_clear = clear_input.get_center()
        center_clear = [center_clear[0] - 27, center_clear[1] - 10]
        print_text(texto = "Clear", screen = display, fonte = font, pos = center_clear, cor = COLOR_BLACK)

        # Recebendo a posição atual do ponteiro do mouse.
        mouse_pos = pygame.mouse.get_pos()

        # Alterando a cor do botão conforme a posição do mouse.
        if download.get_collide(mouse_pos) or box.get_collide(mouse_pos) or clear_input.get_collide(mouse_pos):
            if download.get_collide(mouse_pos):
                download.set_color(COLOR_GRAY)
            elif clear_input.get_collide(mouse_pos):
                clear_input.set_color(COLOR_GRAY)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            download.set_color(COLOR_WHITE)
            clear_input.set_color(COLOR_WHITE)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                run = False


            # Tornando a caixa de entrada ativa.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if box.get_collide(event.pos):
                    box.set_active(True)
                else:
                    box.set_active(False)

                if clear_input.get_collide(event.pos):
                    input_url = ""

                # Quando o botão de download é pressionado
                if download.get_collide(event.pos):
                    input_url.strip() # Corta os espaços em excesso no início e no final (se existirem)
                    video = VideoYT(input_url)
                    title = video.get_title()

                    show_thumbnail(display, video.get_thumbnail_url())
                    title_pos = [box.get_box_x(), box.get_box_y() - 50]
                    
                    
                    print_just_title(text = title, screen = display, fonte = info_font, pos = title_pos, cor = COLOR_WHITE)
                    video.download()
                    



            # Recebendo a entrada do teclado (URL do vídeo)
            elif event.type == pygame.KEYDOWN:
                if box.get_active():
                    keys = pygame.key.get_pressed()

                    # Configurando tecla BACKSPACE para apagar o texto.
                    if event.key == pygame.K_BACKSPACE:
                        if len(input_url):
                            input_url = input_url[0:-1]

                    # Definido CTRL + V para colar a URL na caixa de texto.
                    elif keys[pygame.K_LCTRL] and keys[pygame.K_v]:
                        input_url = pyperclip.paste()
                    
                    # Recebendo o que o usuário digita.
                    else:
                        input_url += event.unicode
            
            
            else: 
                pass


        if run:
            pygame.display.update()

    pygame.quit()