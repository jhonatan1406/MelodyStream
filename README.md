
# 🎵 MelodyStream

**MelodyStream** é uma aplicação de streaming de música desenvolvida em Python que permite aos usuários reproduzir suas músicas favoritas, criar e gerenciar playlists, e explorar um catálogo abrangente de faixas. Com uma interface interativa e funcionalidades robustas, MelodyStream oferece uma experiência musical fluida e personalizada.

## 📋 Índice

- [🎯 Funcionalidades](#🎯-funcionalidades)
- [🛠️ Tecnologias Utilizadas](#🛠️-tecnologias-utilizadas)
- [💾 Instalação](#💾-instalação)
  - [Pré-requisitos](#pré-requisitos)
  - [Passos de Instalação](#passos-de-instalação)
- [🚀 Como Usar](#🚀-como-usar)
  - [📸 Exemplo de Uso](#📸-exemplo-de-uso)
- [🤝 Contribuição](#🤝-contribuição)
- [📄 Licença](#📄-licença)
- [📫 Contato](#📫-contato)

## 🎯 Funcionalidades

- **Reproduzir Músicas**: Selecione e reproduza suas músicas favoritas diretamente na aplicação.
- **Gerenciar Playlists**: Crie, edite e organize playlists personalizadas adicionando suas músicas preferidas.
- **Explorar o Catálogo**: Navegue por um catálogo completo de músicas disponíveis para reprodução.
- **Reprodução Não Bloqueante**: Execute músicas em segundo plano, permitindo que você continue interagindo com a aplicação enquanto a música toca.
- **Interface Interativa**: Utilize um menu intuitivo para navegar pelas diferentes funcionalidades da aplicação.
- **Importação Automática de Músicas**: Adicione todas as músicas de uma pasta específica ao catálogo automaticamente, sem reproduzi-las durante a importação.
- **Navegação na Playlist**: Avance para a próxima música ou volte para a música anterior na playlist em reprodução.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal.
- **Pygame**: Biblioteca utilizada para a reprodução de áudio.
- **Threading**: Para permitir a reprodução não bloqueante das músicas.
- **Outras Bibliotecas**: `os`, `time`, `threading`.

## 💾 Instalação

### Pré-requisitos

- **Python 3.x** instalado em seu sistema.
- **Pygame**: Biblioteca para reprodução de áudio.

### Passos de Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/MelodyStream.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd MelodyStream
   ```

3. **Instale as dependências necessárias:**

   ```bash
   pip install pygame
   ```

4. **Organize suas músicas:**

   - Crie uma pasta para armazenar suas músicas, por exemplo: `C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM`.
   - Adicione os arquivos de áudio (`.mp3`, `.wav`, `.ogg`, `.flac`, etc.) nessa pasta.

5. **Atualize os caminhos das músicas no código (opcional):**

   - Se preferir adicionar músicas manualmente, abra o arquivo `sistema_streaming.py`.
   - No método `adicionar_musicas_iniciais`, adicione instâncias da classe `Musica` com os caminhos corretos dos arquivos de áudio.

## 🚀 Como Usar

1. **Execute a aplicação:**

   ```bash
   python sistema_streaming.py
   ```

2. **Insira o Caminho da Pasta de Músicas:**

   - Quando solicitado, insira o caminho completo para a pasta onde suas músicas estão armazenadas.
   - **Exemplo:** `C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM`

3. **Interaja com o Menu:**

   - **1. Reproduzir uma música**: Digite parte do título da música que deseja ouvir.
   - **2. Criar uma playlist**: Crie uma nova playlist.
   - **3. Adicionar música a uma playlist**: Adicione músicas existentes do catálogo a uma playlist específica.
   - **4. Remover música de uma playlist**: Remova músicas de uma playlist existente.
   - **5. Mostrar informações da playlist**: Visualize as músicas contidas em uma playlist específica.
   - **6. Reproduzir música de uma playlist**: Selecione e reproduza uma música de uma playlist.
   - **7. Próxima música na playlist**: Avance para a próxima música na playlist em reprodução.
   - **8. Música anterior na playlist**: Volte para a música anterior na playlist em reprodução.
   - **9. Listar todas as músicas disponíveis**: Veja todas as músicas disponíveis no catálogo.
   - **10. Parar reprodução atual**: Pare a música que está sendo reproduzida no momento.
   - **11. Sair**: Encerre a aplicação. Qualquer música em reprodução será parada automaticamente.

### 📸 Exemplo de Uso

```
Bem-vindo ao Sistema de Streaming de Música!
Por favor, insira o caminho para a pasta de músicas: C:\Users\Jhonatan\Desktop\TRABALHO LINGUAGEM
Adicionada: Crawling [Official HD Music Video] - Linkin Park
Adicionada: Imagine Dragons - Believer (Official Music Video)
Adicionada: In The End [Official HD Music Video] - Linkin Park
Adicionada: mirros - Desconhecido
Adicionada: Numb (Official Music Video) [4K UPGRADE] – Linkin Park - Desconhecido
Adicionada: NX Zero - Daqui Pra Frente (Tour Cedo ou Tarde Ao Vivo)
Adicionada: Queen – Bohemian Rhapsody (Official Video Remastered) - Desconhecido
Adicionada: Sia - Elastic Heart (TraduçãoLegendas)
Adicionada: The Beatles - Come Together
Adicionada: The Emptiness Machine (Official Music Video) - Linkin Park
Adicionada: The Kinks - You Really Got Me (Official Audio)

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 2
Digite o nome da nova playlist: Favorites
Playlist 'Favorites' criada com sucesso.

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 3
Digite o nome da playlist: Favorites
Digite o título da música para adicionar: In The End

Músicas Encontradas:
1. In The End [Official HD Music Video] - Linkin Park (3.63 minutos)
Escolha o número da música desejada: 1
Música 'In The End [Official HD Music Video]' adicionada à playlist 'Favorites'.

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 6
Digite o nome da playlist: Favorites

Playlist: Favorites
1. In The End [Official HD Music Video] - Linkin Park (3.63 minutos)
Digite o número da música que deseja reproduzir: 1
Iniciando reprodução: In The End [Official HD Music Video] - Linkin Park

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 7
Você está na última música da playlist.

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 8
Parando reprodução de 'In The End [Official HD Music Video] - Linkin Park (3.63 minutos)'.
Nenhuma música está sendo reproduzida.

Sistema de Streaming de Música (Orientado a Objetos)
1. Reproduzir uma música
2. Criar uma playlist
3. Adicionar música a uma playlist
4. Remover música de uma playlist
5. Mostrar informações da playlist
6. Reproduzir música de uma playlist
7. Próxima música na playlist
8. Música anterior na playlist
9. Listar todas as músicas disponíveis
10. Parar reprodução atual
11. Sair
Escolha uma opção: 11
Encerrando o sistema. Até mais!
Nenhuma música está sendo reproduzida.
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

1. **Fork este repositório**
2. **Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)**
3. **Faça o commit das suas mudanças (`git commit -am 'Adiciona nova feature'`)**
4. **Faça o push para a branch (`git push origin feature/nova-feature`)**
5. **Abra um Pull Request**

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📫 Contato

- **Nome**: Jhonatan
- **Email**: [jhonatanalmeida99@gmail.com](mailto:jhonatanalmeida99@gmail.com)
- **LinkedIn**: [linkedin.com/in/jhonatan-almeida-89b52623b](https://www.linkedin.com/in/jhonatan-almeida-89b52623b/)

---

### 🔧 Melhorias Futuras

Para aprimorar ainda mais o seu **MelodyStream**, considere as seguintes melhorias:

1. **Filtros por Gênero:**
   - Adicionar atributos de gênero às músicas e implementar funcionalidades de filtro no catálogo e nas playlists.

2. **Interface Gráfica:**
   - Implementar uma interface gráfica usando bibliotecas como `Tkinter`, `PyQt` ou `Kivy` para tornar a aplicação mais amigável e visualmente atraente.

3. **Controle de Volume:**
   - Adicionar funcionalidades para ajustar o volume da reprodução, permitindo que os usuários personalizem a experiência sonora.

4. **Reprodução Aleatória e Repetição:**
   - Implementar opções de reprodução aleatória e repetição de músicas ou playlists para uma experiência de audição mais dinâmica.

5. **Metadata de Músicas:**
   - Utilizar bibliotecas como `mutagen` para obter metadados mais precisos das músicas, permitindo uma melhor organização e exibição de informações.

6. **Persistência de Dados:**
   - Salvar playlists e configurações em arquivos ou banco de dados para que os usuários não percam suas configurações ao fechar a aplicação.

---