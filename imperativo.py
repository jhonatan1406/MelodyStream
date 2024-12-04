# Sistema de Streaming de Música - Paradigma Imperativo

import pygame
import time
import os

# Inicializar o sistema de áudio
pygame.mixer.init()

# Dados do sistema
catalogo = [
    {"titulo": "Mirrors", "artista": "Justin Timberlake", "duracao": 3.1, "file_path": r"C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\mirros.mp3"},
    {"titulo": "Bohemian Rhapsody", "artista": "Queen", "duracao": 5.55, "file_path": r"C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\bohemian_rhapsody.mp3"},
    {"titulo": "Stairway to Heaven", "artista": "Led Zeppelin", "duracao": 8.02, "file_path": r"C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\stairway_to_heaven.mp3"},
    {"titulo": "Hotel California", "artista": "Eagles", "duracao": 6.3, "file_path": r"C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM\hotel_california.mp3"}
]

playlists = {}
musica_atual = None

# Função para listar o catálogo
def listar_catalogo():
    print("\nCatálogo de Músicas Disponíveis:")
    for i, musica in enumerate(catalogo, start=1):
        print(f"{i}. {musica['titulo']} - {musica['artista']} ({musica['duracao']} minutos)")

# Função para buscar uma música no catálogo
def buscar_musica_por_titulo(titulo_parcial):
    for musica in catalogo:
        if titulo_parcial.lower() in musica["titulo"].lower():
            return musica
    return None

# Função para reproduzir uma música
def reproduzir_musica():
    global musica_atual
    if musica_atual:
        parar_reproducao()

    titulo = input("Digite o título ou parte do título da música: ").strip()
    musica = buscar_musica_por_titulo(titulo)
    if musica:
        print(f"Reproduzindo: {musica['titulo']} - {musica['artista']}")
        if os.path.exists(musica["file_path"]):
            pygame.mixer.music.load(musica["file_path"])
            pygame.mixer.music.play()
            musica_atual = musica
        else:
            print("Erro: Arquivo de áudio não encontrado.")
    else:
        print("Música não encontrada no catálogo.")

# Função para parar a reprodução
def parar_reproducao():
    global musica_atual
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print(f"Parando reprodução: {musica_atual['titulo']}")
        musica_atual = None
    else:
        print("Nenhuma música está sendo reproduzida.")

# Função para criar uma playlist
def criar_playlist():
    nome = input("Digite o nome da playlist: ").strip()
    if nome in playlists:
        print("Erro: Playlist com esse nome já existe.")
    else:
        playlists[nome] = []
        print(f"Playlist '{nome}' criada com sucesso.")

# Função para adicionar música a uma playlist
def adicionar_musica_playlist():
    nome = input("Digite o nome da playlist: ").strip()
    if nome not in playlists:
        print("Erro: Playlist não encontrada.")
        return

    titulo = input("Digite o título da música para adicionar: ").strip()
    musica = buscar_musica_por_titulo(titulo)
    if musica:
        playlists[nome].append(musica)
        print(f"Música '{musica['titulo']}' adicionada à playlist '{nome}'.")
    else:
        print("Música não encontrada no catálogo.")

# Função para exibir as músicas de uma playlist
def exibir_playlist():
    nome = input("Digite o nome da playlist: ").strip()
    if nome not in playlists:
        print("Erro: Playlist não encontrada.")
        return

    print(f"\nPlaylist: {nome}")
    for i, musica in enumerate(playlists[nome], start=1):
        print(f"{i}. {musica['titulo']} - {musica['artista']}")

# Função para reproduzir música de uma playlist
def reproduzir_musica_playlist():
    nome = input("Digite o nome da playlist: ").strip()
    if nome not in playlists:
        print("Erro: Playlist não encontrada.")
        return

    exibir_playlist()
    try:
        escolha = int(input("Digite o número da música que deseja reproduzir: "))
        if 1 <= escolha <= len(playlists[nome]):
            musica = playlists[nome][escolha - 1]
            global musica_atual
            if musica_atual:
                parar_reproducao()
            print(f"Reproduzindo: {musica['titulo']} - {musica['artista']}")
            if os.path.exists(musica["file_path"]):
                pygame.mixer.music.load(musica["file_path"])
                pygame.mixer.music.play()
                musica_atual = musica
            else:
                print("Erro: Arquivo de áudio não encontrado.")
        else:
            print("Erro: Escolha inválida.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

# Menu principal
def menu():
    while True:
        print("\nSistema de Streaming de Música - Paradigma Imperativo")
        print("1. Reproduzir uma música")
        print("2. Criar uma playlist")
        print("3. Adicionar música a uma playlist")
        print("4. Exibir uma playlist")
        print("5. Reproduzir música de uma playlist")
        print("6. Listar todas as músicas do catálogo")
        print("7. Parar reprodução")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            reproduzir_musica()
        elif escolha == "2":
            criar_playlist()
        elif escolha == "3":
            adicionar_musica_playlist()
        elif escolha == "4":
            exibir_playlist()
        elif escolha == "5":
            reproduzir_musica_playlist()
        elif escolha == "6":
            listar_catalogo()
        elif escolha == "7":
            parar_reproducao()
        elif escolha == "8":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Erro: Opção inválida. Tente novamente.")

# Executar o sistema
menu()
