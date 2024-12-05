# MelodyStream - Sistema de Streaming de Música em Python (Paradigma Imperativo)

import pygame
import threading
import time
import os

# Inicializa o mixer do pygame uma vez no início
pygame.mixer.init()

# Variáveis globais para controle da reprodução
musica_atual = None
play_thread = None
is_playing = False
lock = threading.Lock()
current_playlist = None
current_index = 0

def exibir_menu():
    print("\nSistema de Streaming de Música (Imperativo)")
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

def reproduzir_musica(catalogo, playlist=None, index=0):
    global musica_atual, play_thread, is_playing, current_playlist, current_index

    if is_playing:
        parar_reproducao()

    if playlist:
        if not playlist:
            print("A playlist está vazia.")
            return
        if index < 0 or index >= len(playlist):
            print("Índice inválido.")
            return
        musica = playlist[index]
        current_playlist = playlist
        current_index = index
    else:
        titulo = input("Digite parte do título da música que deseja reproduzir: ").strip()
        if not titulo:
            print("Erro: O título da música não pode estar vazio.")
            return
        # Busca por título parcial
        resultados = [m for m in catalogo if titulo.lower() in m['titulo'].lower()]
        if not resultados:
            print("Música não encontrada no catálogo.")
            return
        elif len(resultados) == 1:
            musica = resultados[0]
            current_playlist = None
            current_index = 0
        else:
            print("\nMúsicas Encontradas:")
            for idx, m in enumerate(resultados, 1):
                print(f"{idx}. {m['titulo']} - {m['artista']} ({m['duracao']} minutos)")
            while True:
                try:
                    escolha = int(input("Escolha o número da música desejada: "))
                    if 1 <= escolha <= len(resultados):
                        musica = resultados[escolha - 1]
                        current_playlist = None
                        current_index = 0
                        break
                    else:
                        print("Erro: Escolha inválida.")
                except ValueError:
                    print("Erro: Por favor, digite um número válido.")

    def play():
        global is_playing
        try:
            pygame.mixer.music.load(musica['file_path'])
            pygame.mixer.music.play()
            is_playing = True
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_playing = False
        except Exception as e:
            print(f"Erro ao reproduzir a música: {e}")
            is_playing = False

    musica_atual = musica
    print(f"Iniciando reprodução: {musica['titulo']} - {musica['artista']}")
    play_thread = threading.Thread(target=play, daemon=True)
    play_thread.start()

def parar_reproducao():
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
        print(f"Reprodução de '{musica_atual['titulo']}' parada.")
    else:
        print("Nenhuma música está sendo reproduzida.")

def criar_playlist(playlists):
    nome_playlist = input("Digite o nome da nova playlist: ").strip()
    if not nome_playlist:
        print("Erro: O nome da playlist não pode estar vazio.")
        return
    if nome_playlist in playlists:
        print("Erro: Uma playlist com este nome já existe.")
        return
    playlists[nome_playlist] = []
    print(f"Playlist '{nome_playlist}' criada com sucesso.")

def adicionar_playlist(playlists, catalogo):
    nome_playlist = input("Digite o nome da playlist: ").strip()
    if not nome_playlist:
        print("Erro: O nome da playlist não pode estar vazio.")
        return
    if nome_playlist not in playlists:
        print("Erro: Playlist não encontrada.")
        return
    while True:
        titulo = input("Digite o título da música para adicionar (ou 'sair' para finalizar): ").strip()
        if titulo.lower() == 'sair':
            break
        if not titulo:
            print("Erro: O título da música não pode estar vazio.")
            continue
        # Busca por título exato
        musica = next((m for m in catalogo if m['titulo'].lower() == titulo.lower()), None)
        if musica:
            playlists[nome_playlist].append(musica)
            print(f"Música '{musica['titulo']}' adicionada à playlist '{nome_playlist}'.")
        else:
            print("Música não encontrada no catálogo.")

def remover_musica_playlist(playlists):
    nome_playlist = input("Digite o nome da playlist: ").strip()
    if not nome_playlist:
        print("Erro: O nome da playlist não pode estar vazio.")
        return
    if nome_playlist not in playlists:
        print("Erro: Playlist não encontrada.")
        return
    if not playlists[nome_playlist]:
        print(f"A playlist '{nome_playlist}' está vazia.")
        return
    print(f"\nPlaylist: {nome_playlist}")
    for idx, musica in enumerate(playlists[nome_playlist], 1):
        print(f"{idx}. {musica['titulo']} - {musica['artista']} ({musica['duracao']} minutos)")
    try:
        escolha = int(input("Digite o número da música que deseja remover: "))
        if 1 <= escolha <= len(playlists[nome_playlist]):
            musica_removida = playlists[nome_playlist].pop(escolha - 1)
            print(f"Música '{musica_removida['titulo']}' removida da playlist '{nome_playlist}'.")
        else:
            print("Erro: Escolha inválida.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

def mostrar_playlist(playlists):
    nome_playlist = input("Digite o nome da playlist que deseja visualizar: ").strip()
    if not nome_playlist:
        print("Erro: O nome da playlist não pode estar vazio.")
        return
    if nome_playlist in playlists:
        if not playlists[nome_playlist]:
            print(f"A playlist '{nome_playlist}' está vazia.")
            return
        print(f"\nPlaylist: {nome_playlist}")
        for idx, musica in enumerate(playlists[nome_playlist], 1):
            print(f"{idx}. {musica['titulo']} - {musica['artista']} ({musica['duracao']} minutos)")
    else:
        print("Playlist não encontrada.")

def reproduzir_musica_playlist(playlists):
    global current_playlist, current_index
    nome_playlist = input("Digite o nome da playlist: ").strip()
    if not nome_playlist:
        print("Erro: O nome da playlist não pode estar vazio.")
        return
    if nome_playlist not in playlists:
        print("Erro: Playlist não encontrada.")
        return
    if not playlists[nome_playlist]:
        print("A playlist está vazia.")
        return
    print(f"\nPlaylist: {nome_playlist}")
    for idx, musica in enumerate(playlists[nome_playlist], 1):
        print(f"{idx}. {musica['titulo']} - {musica['artista']} ({musica['duracao']} minutos)")
    try:
        escolha = int(input("Digite o número da música que deseja reproduzir: "))
        if 1 <= escolha <= len(playlists[nome_playlist]):
            current_playlist = playlists[nome_playlist]
            current_index = escolha - 1
            musica = current_playlist[current_index]
            reproduzir_musica(current_playlist, playlist=current_playlist, index=current_index)
        else:
            print("Erro: Escolha inválida.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

def next_song(playlists):
    global current_playlist, current_index
    if not current_playlist:
        print("Erro: Nenhuma playlist está sendo reproduzida atualmente.")
        return
    if current_index + 1 >= len(current_playlist):
        print("Você está na última música da playlist.")
        return
    parar_reproducao()
    current_index += 1
    musica = current_playlist[current_index]
    print(f"Iniciando reprodução: {musica['titulo']} - {musica['artista']}")
    reproduzir_musica(current_playlist, playlist=current_playlist, index=current_index)

def previous_song(playlists):
    global current_playlist, current_index
    if not current_playlist:
        print("Erro: Nenhuma playlist está sendo reproduzida atualmente.")
        return
    if current_index - 1 < 0:
        print("Você está na primeira música da playlist.")
        return
    parar_reproducao()
    current_index -= 1
    musica = current_playlist[current_index]
    print(f"Iniciando reprodução: {musica['titulo']} - {musica['artista']}")
    reproduzir_musica(current_playlist, playlist=current_playlist, index=current_index)

def listar_catalogo(catalogo):
    if not catalogo:
        print("O catálogo está vazio.")
    else:
        print("\nCatálogo de Músicas Disponíveis:")
        for idx, musica in enumerate(catalogo, 1):
            print(f"{idx}. {musica['titulo']} - {musica['artista']} ({musica['duracao']} minutos)")

def adicionar_musicas_iniciais(catalogo, music_dir):
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
                    duracao = round(sound.get_length() / 60, 2)  # duração em minutos
                except Exception as e:
                    print(f"Erro ao obter duração de '{file}': {e}")
                    duracao = 0.0  # Duração desconhecida

                musica = {'titulo': titulo.strip(), 'artista': artista.strip(), 'duracao': duracao, 'file_path': file_path}
                catalogo.append(musica)
                print(f"Adicionada: {musica['titulo']} - {musica['artista']}")

def main():
    global musica_atual, play_thread, is_playing, current_playlist, current_index
    catalogo = []
    playlists = {}

    print("Bem-vindo ao Sistema de Streaming de Música!")
    music_dir = input("Por favor, insira o caminho para a pasta de músicas: ").strip()

    if not music_dir:
        print("Erro: O caminho da pasta de músicas não pode estar vazio.")
        return

    adicionar_musicas_iniciais(catalogo, music_dir)

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            reproduzir_musica(catalogo)
        elif escolha == '2':
            criar_playlist(playlists)
        elif escolha == '3':
            adicionar_playlist(playlists, catalogo)
        elif escolha == '4':
            remover_musica_playlist(playlists)
        elif escolha == '5':
            mostrar_playlist(playlists)
        elif escolha == '6':
            reproduzir_musica_playlist(playlists)
        elif escolha == '7':
            next_song(playlists)
        elif escolha == '8':
            previous_song(playlists)
        elif escolha == '9':
            listar_catalogo(catalogo)
        elif escolha == '10':
            parar_reproducao()
        elif escolha == '11':
            print("Encerrando o sistema. Até mais!")
            parar_reproducao()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
