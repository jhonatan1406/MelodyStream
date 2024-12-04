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
        self.file_path = file_path
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

    def exibir_menu(self):
        print("\nSistema de Streaming de Música (Orientado a Objetos)")
        print("1. Reproduzir uma música")
        print("2. Criar uma playlist")
        print("3. Adicionar música a uma playlist")
        print("4. Remover música de uma playlist")
        print("5. Mostrar informações da playlist")
        print("6. Reproduzir música de uma playlist")
        print("7. Listar todas as músicas disponíveis")
        print("8. Parar reprodução atual")
        print("9. Sair")

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
        try:
            escolha = int(input("Digite o número da música que deseja reproduzir: "))
            if 1 <= escolha <= len(playlist.musicas):
                if self.musica_atual and self.musica_atual.esta_tocando():
                    print(f"Parando reprodução de: {self.musica_atual.titulo}")
                    self.musica_atual.parar_reproducao()
                self.musica_atual = playlist.musicas[escolha - 1]
                self.musica_atual.reproduzir()
            else:
                print("Erro: Escolha inválida.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

    def listar_catalogo(self):
        self.catalogo.listar_musicas()

    def parar_reproducao_atual(self):
        if self.musica_atual and self.musica_atual.esta_tocando():
            self.musica_atual.parar_reproducao()
        else:
            print("Nenhuma música está sendo reproduzida.")

    def adicionar_musicas_iniciais(self):
        try:
            self.catalogo.adicionar_musica(Musica('mirros', 'Justin', 3.1, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\mirros.mp3'))
            self.catalogo.adicionar_musica(Musica('Bohemian Rhapsody', 'Queen', 5.55, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\bohemian_rhapsody.mp3'))
            self.catalogo.adicionar_musica(Musica('Stairway to Heaven', 'Led Zeppelin', 8.02, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\stairway_to_heaven.mp3'))
            self.catalogo.adicionar_musica(Musica('Hotel California', 'Eagles', 6.30, r'C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\hotel_california.mp3'))
        except Exception as e:
            print(f"Erro ao adicionar músicas iniciais: {e}")

    def executar(self):
        self.adicionar_musicas_iniciais()
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
                self.listar_catalogo()
            elif escolha == '8':
                self.parar_reproducao_atual()
            elif escolha == '9':
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
