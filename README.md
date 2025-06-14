<div align="center">

<h1>Transcritor de Áudio</h1>

Transcritor de áudios e vídeos para o formato .docx

<img src="/Animação.gif" />

</div>

---

## Sobre o Projeto

O projeto de Transcritor de Áudio teve como objetivo criar uma aplicação capaz de: 
- Receber qualquer áudio ou vídeo, realizar o processo de transcrição, gerar um arquivo .docx com o texto transcrito e salvar em qualquer local do seu computador. 

## Motivo para Criação do Projeto

O motivo para criar este projeto foi uma forma de estudo, prática de programação, peça de portifólio para demonstrar capacidades e aplicar conceitos de APIs, interface gráfica, manipulação de arquivos e dados.

## Tecnologias utilizadas

- **Python:** Linguagem principal de programação do projeto.
- **Tkinter:** Biblioteca padrão do Python para a criação da interface gráfica (GUI).
- **SpeechRecognition:** Biblioteca utilizada para realizar o reconhecimento de fala e a transcrição, utilizando a API do Google.
- **Pydub:** Usada para manipular arquivos de áudio, permitindo a conversão de diferentes formatos para `.wav`.

## Instalação e Configuração

Instalação e Configuração
Siga os passos abaixo para configurar o ambiente e executar o projeto em sua máquina local.

### 1. Pré-requisitos
Antes de começar, certifique-se de que você tem os seguintes softwares instalados:

- **Python:** Versão 3.10 ou superior. Você pode baixá-lo em python.org.
- **Git:** Para clonar o repositório. Você pode baixá-lo em git-scm.com.
- **FFmpeg:** (Dependência Crítica) A biblioteca pydub precisa do FFmpeg para converter os diferentes formatos de áudio (como MP3, M4A, etc.).

---

- **Windows:**
    A maneira mais fácil é usando o gerenciador de pacotes Chocolatey. Abra o PowerShell como Administrador e execute:
### PowerShell
```powershell
choco install ffmpeg
```
Alternativamente, baixe o FFmpeg do [site oficial](https://ffmpeg.org/download.html) e adicione a pasta bin ao PATH do seu sistema manualmente.

- **macOS:**
    Use o gerenciador de pacotes Homebrew:
### Bash
```bash
brew install ffmpeg
```

- **Linux (Debian/Ubuntu):**
    Use o gerenciador de pacotes APT:

### Bash
```bash
sudo apt update && sudo apt install ffmpeg
```


### 2. Passo a Passo da Instalação

**Clone o Repositório**
Abra seu terminal ou Git Bash e clone este repositório para sua máquina local.

### Bash
```bash
git clone https://github.com/Jodo-Lupi/TranscritorDeAudio.git
cd TranscritorDeAudio
```

**Crie e Ative um Ambiente Virtual**
É uma boa prática isolar as dependências do projeto. Dentro da pasta do projeto, execute:

### Bash
```bash
# Cria o ambiente virtual
python -m venv venv
```
Em seguida, ative-o:

### Bash
```bash
# No Windows
.\venv\Scripts\activate

# No macOS ou Linux
source venv/bin/activate
```
Você saberá que funcionou quando vir (venv) no início da linha do seu terminal.

**Instale as Dependências**
Com o ambiente virtual ativo, instale todas as bibliotecas listadas no requerimentos.txt com um único comando:

### Bash
```bash
pip install -r requerimentos.txt
```

## Como Usar

Execute o programa, clique em ***Selecionar Arquivo de Áudio*** e abrirá uma janela para escolher um arquivo. Selecionando o arquivo, o caminho e nome do arquivo apareceram na tela. Clique no botão ***Transcrever*** e escolha um local de salvamento, após isso iniciará o processo de transcrição e geração do arquivo .docx. 
Você também utilizar dois modos da interface gráfica, o ***Modo Claro*** e ***Modo Escuro***.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](/LICENSE) para mais detalhes.
