# Sistema de Streaming de Música - Paradigma Orientado a Objetos com Reprodução Não Bloqueante

import pygame
import threading
import time
import os

class Musica:
    def __init__(self, titulo, artista, duracao, file_path):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.file_path = file_path  # Caminho do arquivo de áudio
        self._is_playing = False
        self._play_thread = None

    def exibir_info(self):
        print(f"{self.titulo} - {self.artista} ({self.duracao} minutos)")

    def _play_music(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
            self._is_playing = True
            while pygame.mixer.music.get_busy():
                time.sleep(1)  # Aguarda enquanto a música está tocando
            self._is_playing = False
        except Exception as e:
            print(f"Erro ao reproduzir a música: {e}")
            self._is_playing = False

    def reproduzir(self):
        if not os.path.exists(self.file_path):
            print("Arquivo de áudio não encontrado.")
            return
        if self._is_playing:
            print("Uma música já está sendo reproduzida.")
            return
        print(f"Iniciando reprodução: {self.titulo} - {self.artista}")
        self._play_thread = threading.Thread(target=self._play_music, daemon=True)
        self._play_thread.start()

    def parar_reproducao(self):
        if self._is_playing:
            pygame.mixer.music.stop()
            self._is_playing = False
            print(f"Reprodução de '{self.titulo}' parada.")
        else:
            print("Nenhuma música está sendo reproduzida.")

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"Música '{musica.titulo}' adicionada à playlist '{self.nome}'.")

    def exibir_playlist(self):
        print(f"\nPlaylist: {self.nome}")
        for idx, musica in enumerate(self.musicas, 1):
            print(f"{idx}. ", end="")
            musica.exibir_info()

class Catalogo:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def listar_musicas(self):
        print("\nCatálogo de Músicas Disponíveis:")
        for idx, musica in enumerate(self.musicas, 1):
            print(f"{idx}. ", end="")
            musica.exibir_info()

    def buscar_musica(self, titulo):
        for musica in self.musicas:
            if musica.titulo.lower() == titulo.lower():
                return musica
        return None

class SistemaStreaming:
    def __init__(self):
        self.catalogo = Catalogo()
        self.playlists = {}

    def exibir_menu(self):
        print("\nSistema de Streaming de Música (Orientado a Objetos)")
        print("1. Reproduzir uma música")
        print("2. Adicionar música a uma playlist")
        print("3. Mostrar informações da playlist")
        print("4. Listar todas as músicas disponíveis")
        print("5. Parar reprodução atual")
        print("6. Sair")

    def reproduzir_musica(self):
        titulo = input("Digite o título da música que deseja reproduzir: ")
        musica = self.catalogo.buscar_musica(titulo)
        if musica:
            musica.reproduzir()
        else:
            print("Música não encontrada no catálogo.")

    def adicionar_playlist(self):
        nome_playlist = input("Digite o nome da nova playlist: ")
        if nome_playlist in self.playlists:
            print("Playlist já existe.")
            return
        playlist = Playlist(nome_playlist)
        self.playlists[nome_playlist] = playlist
        while True:
            titulo = input("Digite o título da música para adicionar (ou 'sair' para finalizar): ")
            if titulo.lower() == 'sair':
                break
            musica = self.catalogo.buscar_musica(titulo)
            if musica:
                playlist.adicionar_musica(musica)
            else:
                print("Música não encontrada no catálogo.")

    def mostrar_playlist(self):
        nome_playlist = input("Digite o nome da playlist que deseja visualizar: ")
        if nome_playlist in self.playlists:
            self.playlists[nome_playlist].exibir_playlist()
        else:
            print("Playlist não encontrada.")

    def listar_catalogo(self):
        self.catalogo.listar_musicas()

    def parar_reproducao_atual(self):
        # Itera por todas as músicas no catálogo para encontrar qual está sendo reproduzida
        for musica in self.catalogo.musicas:
            if musica._is_playing:
                musica.parar_reproducao()
                return
        print("Nenhuma música está sendo reproduzida.")

    def adicionar_musicas_iniciais(self):
        # Adicionando músicas ao catálogo
        # Atualize os caminhos dos arquivos de áudio conforme seu sistema
        self.catalogo.adicionar_musica(Musica('mirros', 'Justin', 3.1, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\mirros.mp3'))
        self.catalogo.adicionar_musica(Musica('Bohemian Rhapsody', 'Queen', 5.55, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\bohemian_rhapsody.mp3'))
        self.catalogo.adicionar_musica(Musica('Stairway to Heaven', 'Led Zeppelin', 8.02, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\stairway_to_heaven.mp3'))
        self.catalogo.adicionar_musica(Musica('Hotel California', 'Eagles', 6.30, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\hotel_california.mp3'))

    def executar(self):
        self.adicionar_musicas_iniciais()
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.reproduzir_musica()
            elif escolha == '2':
                self.adicionar_playlist()
            elif escolha == '3':
                self.mostrar_playlist()
            elif escolha == '4':
                self.listar_catalogo()
            elif escolha == '5':
                self.parar_reproducao_atual()
            elif escolha == '6':
                print("Encerrando o sistema. Até mais!")
                # Certifique-se de parar qualquer música que esteja tocando antes de sair
                self.parar_reproducao_atual()
                break
            else:
                print("Opção inválida. Tente novamente.")

def main():
    sistema = SistemaStreaming()
    sistema.executar()

if __name__ == "__main__":
    main()
