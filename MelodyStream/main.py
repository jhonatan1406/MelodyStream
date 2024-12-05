# MelodyStream - Sistema de Streaming de Música em Python

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

    def _setup_player(self):
        """Inicializa o mixer apenas se necessário."""
        if not pygame.mixer.get_init():
            pygame.mixer.init()

    def _play_music(self):
        try:
            self._setup_player()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
            self._is_playing = True
            while pygame.mixer.music.get_busy():
                time.sleep(1)
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

    def esta_tocando(self):
        """Verifica se a música está em reprodução."""
        return self._is_playing


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"Música '{musica.titulo}' adicionada à playlist '{self.nome}'.")

    def remover_musica(self, indice):
        if 0 <= indice < len(self.musicas):
            musica = self.musicas.pop(indice)
            print(f"Música '{musica.titulo}' removida da playlist '{self.nome}'.")
        else:
            print("Erro: Índice inválido.")

    def exibir_playlist(self):
        if not self.musicas:
            print(f"A playlist '{self.nome}' está vazia.")
            return
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
        if not self.musicas:
            print("O catálogo está vazio.")
        else:
            print("\nCatálogo de Músicas Disponíveis:")
            for idx, musica in enumerate(self.musicas, 1):
                print(f"{idx}. ", end="")
                musica.exibir_info()

    def buscar_musica(self, busca):
        """Busca músicas por título parcial."""
        resultados = [musica for musica in self.musicas if busca.lower() in musica.titulo.lower()]
        if resultados:
            print("\nMúsicas Encontradas:")
            for idx, musica in enumerate(resultados, 1):
                print(f"{idx}. ", end="")
                musica.exibir_info()
            while True:
                try:
                    escolha = int(input("Escolha o número da música desejada: "))
                    if 1 <= escolha <= len(resultados):
                        return resultados[escolha - 1]
                    else:
                        print("Erro: Escolha inválida.")
                except ValueError:
                    print("Erro: Por favor, digite um número válido.")
        else:
            print("Nenhuma música encontrada com esse título.")
            return None


class SistemaStreaming:
    def __init__(self):
        self.catalogo = Catalogo()
        self.playlists = {}
        self.musica_atual = None
        self.current_playlist = None
        self.current_index = 0
        pygame.mixer.init()  # Inicializa o mixer uma vez no início

    def exibir_menu(self):
        print("\nSistema de Streaming de Música (Orientado a Objetos)")
        print("1. Reproduzir uma música")
        print("2. Criar uma playlist")
        print("3. Adicionar música a uma playlist")
        print("4. Remover música de uma playlist")
        print("5. Mostrar informações da playlist")
        print("6. Reproduzir música de uma playlist")
        print("7. Próxima música na playlist")
        print("8. Música anterior na playlist")
        print("9. Listar todas as músicas disponíveis")
        print("10. Parar reprodução atual")
        print("11. Sair")

    def reproduzir_musica(self):
        if self.musica_atual and self.musica_atual.esta_tocando():
            print(f"Parando reprodução de: {self.musica_atual.titulo}")
            self.musica_atual.parar_reproducao()

        busca = input("Digite parte do título da música que deseja reproduzir: ").strip()
        if not busca:
            print("Erro: O título da música não pode estar vazio.")
            return

        musica = self.catalogo.buscar_musica(busca)
        if musica:
            self.musica_atual = musica
            self.current_playlist = None
            self.current_index = 0
            musica.reproduzir()
        else:
            print("Música não encontrada no catálogo.")

    def criar_playlist(self):
        nome_playlist = input("Digite o nome da nova playlist: ").strip()
        if not nome_playlist:
            print("Erro: O nome da playlist não pode estar vazio.")
            return
        if nome_playlist in self.playlists:
            print("Erro: Uma playlist com este nome já existe.")
            return
        self.playlists[nome_playlist] = Playlist(nome_playlist)
        print(f"Playlist '{nome_playlist}' criada com sucesso.")

    def adicionar_playlist(self):
        nome_playlist = input("Digite o nome da playlist: ").strip()
        if nome_playlist not in self.playlists:
            print("Erro: Playlist não encontrada.")
            return
        playlist = self.playlists[nome_playlist]

        titulo = input("Digite o título da música para adicionar: ").strip()
        if not titulo:
            print("Erro: O título da música não pode estar vazio.")
            return
        musica = self.catalogo.buscar_musica(titulo)
        if musica:
            playlist.adicionar_musica(musica)
        else:
            print("Música não encontrada no catálogo.")

    def remover_musica_playlist(self):
        nome_playlist = input("Digite o nome da playlist: ").strip()
        if nome_playlist not in self.playlists:
            print("Erro: Playlist não encontrada.")
            return
        playlist = self.playlists[nome_playlist]

        playlist.exibir_playlist()
        if not playlist.musicas:
            return
        try:
            escolha = int(input("Digite o número da música que deseja remover: "))
            if 1 <= escolha <= len(playlist.musicas):
                musica_removida = playlist.musicas.pop(escolha - 1)
                print(f"Música '{musica_removida.titulo}' removida da playlist '{nome_playlist}'.")
            else:
                print("Erro: Escolha inválida.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

    def mostrar_playlist(self):
        nome_playlist = input("Digite o nome da playlist que deseja visualizar: ").strip()
        if not nome_playlist:
            print("Erro: O nome da playlist não pode estar vazio.")
            return

        if nome_playlist in self.playlists:
            self.playlists[nome_playlist].exibir_playlist()
        else:
            print("Erro: Playlist não encontrada.")

    def reproduzir_musica_playlist(self):
        nome_playlist = input("Digite o nome da playlist: ").strip()
        if nome_playlist not in self.playlists:
            print("Erro: Playlist não encontrada.")
            return
        playlist = self.playlists[nome_playlist]

        playlist.exibir_playlist()
        if not playlist.musicas:
            return
        try:
            escolha = int(input("Digite o número da música que deseja reproduzir: "))
            if 1 <= escolha <= len(playlist.musicas):
                if self.musica_atual and self.musica_atual.esta_tocando():
                    print(f"Parando reprodução de: {self.musica_atual.titulo}")
                    self.musica_atual.parar_reproducao()
                self.current_playlist = playlist
                self.current_index = escolha - 1
                self.musica_atual = playlist.musicas[self.current_index]
                self.musica_atual.reproduzir()
            else:
                print("Erro: Escolha inválida.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

    def next_song(self):
        if not self.current_playlist:
            print("Erro: Nenhuma playlist está sendo reproduzida atualmente.")
            return
        if self.current_index + 1 >= len(self.current_playlist.musicas):
            print("Você está na última música da playlist.")
            return
        if self.musica_atual and self.musica_atual.esta_tocando():
            self.musica_atual.parar_reproducao()
        self.current_index += 1
        self.musica_atual = self.current_playlist.musicas[self.current_index]
        print(f"Iniciando reprodução: {self.musica_atual.titulo} - {self.musica_atual.artista}")
        self.musica_atual.reproduzir()

    def previous_song(self):
        if not self.current_playlist:
            print("Erro: Nenhuma playlist está sendo reproduzida atualmente.")
            return
        if self.current_index - 1 < 0:
            print("Você está na primeira música da playlist.")
            return
        if self.musica_atual and self.musica_atual.esta_tocando():
            self.musica_atual.parar_reproducao()
        self.current_index -= 1
        self.musica_atual = self.current_playlist.musicas[self.current_index]
        print(f"Iniciando reprodução: {self.musica_atual.titulo} - {self.musica_atual.artista}")
        self.musica_atual.reproduzir()

    def listar_catalogo(self):
        self.catalogo.listar_musicas()

    def parar_reproducao_atual(self):
        if self.musica_atual and self.musica_atual.esta_tocando():
            self.musica_atual.parar_reproducao()
            self.current_playlist = None
            self.current_index = 0
        else:
            print("Nenhuma música está sendo reproduzida.")

    def adicionar_musicas_iniciais(self, music_dir):
        # Verifica se o diretório existe
        if not os.path.isdir(music_dir):
            print(f"O diretório '{music_dir}' não existe. Por favor, verifique o caminho.")
            return

        # Suporte a formatos de áudio comuns
        formatos_audio = ('.mp3', '.wav', '.ogg', '.flac')

        # Lista todos os arquivos no diretório e subdiretórios
        for root, dirs, files in os.walk(music_dir):
            for file in files:
                if file.lower().endswith(formatos_audio):
                    file_path = os.path.join(root, file)
                    # Extrai título e artista a partir do nome do arquivo (assumindo o formato "Título - Artista.ext")
                    nome_arquivo = os.path.splitext(file)[0]
                    if ' - ' in nome_arquivo:
                        titulo, artista = nome_arquivo.split(' - ', 1)
                    else:
                        titulo = nome_arquivo
                        artista = 'Desconhecido'

                    # Tentativa de obter a duração da música sem reproduzi-la
                    try:
                        sound = pygame.mixer.Sound(file_path)
                        duracao = sound.get_length() / 60  # duração em minutos
                    except Exception as e:
                        print(f"Erro ao obter duração de '{file}': {e}")
                        duracao = 0.0  # Duração desconhecida

                    musica = Musica(titulo.strip(), artista.strip(), round(duracao, 2), file_path)
                    self.catalogo.adicionar_musica(musica)
                    print(f"Adicionada: {musica.titulo} - {musica.artista}")

    def executar(self):
        print("Bem-vindo ao Sistema de Streaming de Música!")
        music_dir = input("Por favor, insira o caminho para a pasta de músicas: ").strip()

        if not music_dir:
            print("Erro: O caminho da pasta de músicas não pode estar vazio.")
            return

        self.adicionar_musicas_iniciais(music_dir)

        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                self.reproduzir_musica()
            elif escolha == '2':
                self.criar_playlist()
            elif escolha == '3':
                self.adicionar_playlist()
            elif escolha == '4':
                self.remover_musica_playlist()
            elif escolha == '5':
                self.mostrar_playlist()
            elif escolha == '6':
                self.reproduzir_musica_playlist()
            elif escolha == '7':
                self.next_song()
            elif escolha == '8':
                self.previous_song()
            elif escolha == '9':
                self.listar_catalogo()
            elif escolha == '10':
                self.parar_reproducao_atual()
            elif escolha == '11':
                print("Encerrando o sistema. Até mais!")
                self.parar_reproducao_atual()
                break
            else:
                print("Opção inválida. Tente novamente.")


def main():
    sistema = SistemaStreaming()
    sistema.executar()


if __name__ == "__main__":
    main()
