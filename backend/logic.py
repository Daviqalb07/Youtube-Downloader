from pytube import YouTube
import os
import platform

# Representa a classe YouTube no arquivo main.py
class VideoYT:
    def __init__(self, link: str):
        self.yt = YouTube(link)

    # Retorna o título do vídeo.
    def get_title(self):
        return self.yt.title

    # Retorna a URL da thumbnail do vídeo.
    def get_thumbnail_url(self):
        return self.yt.thumbnail_url

    # Baixa o vídeo.
    def download(self):
        plataforma = platform.system() # Obtém o sistema operacional

        path = os.getcwd()
        # De acordo com o S.O. cria a pasta de arquivo com os separadores adequados.
        if plataforma == "Windows":
            path = path + "\\videos"
        elif plataforma == "Linux":
            path = path + "/videos"

        # Baixa o vídeo com a maior resolução.
        self.yt.streams.get_highest_resolution().download(path)
