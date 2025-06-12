import os
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from conversor import conversorAutomaticoDeAudio
from transcritor import transcrever_audio

os.system("cls")

#Função responsavel por selecionar um arquivo
def selecionar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecione um arquivo")
    caminho_var.set(caminho)

def atualizar_progress_bar(progresso):
    """Simula um carregamento para a barra de progresso."""
    progress_var.set(progresso)
    root.update_idletasks()

#função responsável por utilizar a função de transcrever e abrir um arquivo novo
def iniciar_transcritor():
    btn_transcrever.config(state=tk.DISABLED)  # Desabilitar botão enquanto processa
    caminho = caminho_var.get()
    if (caminho and caminho != "Nenhum arquivo selecionado"):
        if not(caminho.endswith('.wav')):
            caminho = conversorAutomaticoDeAudio(caminho)
        # Iniciar a thread da transcrição
        thread_transcricao = threading.Thread(target=executar_transcritor, args=(caminho,), daemon=True)
        thread_transcricao.start()
    else: 
        messagebox.showerror("Erro", "Nenhum arquivo selecionado! Escolha um arquivo de áudio antes de continuar.")
    
def executar_transcritor(_caminho):
    def callback_progresso(progresso):
        atualizar_progress_bar(progresso)
        
    #Escolha do local de salvamento
    caminho = filedialog.askdirectory(title="Escolha o local de salvamento")
    #Chamada da função responsável por transcrever
    texto_transcrito = transcrever_audio(_caminho, callback=callback_progresso)
    #Escrevendo transcrição em um novo arquivo
    caminho_original = caminho_var.get()
    _, ext = os.path.splitext(caminho_original)
    ext = ext.lower()
    caminho_transcricao = os.path.join(caminho, os.path.basename(caminho_original).replace(ext, ".docx"))

    with open(caminho_transcricao, "w") as file:
        file.write(texto_transcrito)
    
    # Finaliza a barra de progresso e exibe mensagem de conclusão
    atualizar_progress_bar(100)
    messagebox.showinfo("Sucesso", f"Transcrição salva em:\n{caminho}")
    btn_transcrever.config(state=tk.NORMAL)  # Reabilitar botão após conclusão

def aplicar_modo_escuro():
    # Cores
    BG_COLOR = '#2E2E2E'
    FG_COLOR = '#FFFFFF'
    BTN_COLOR = '#3C3C3C'
    ACCENT_COLOR = '#0078D7'

    # Aplica cores ao root e frames
    root.configure(bg=BG_COLOR)
    main_frame.configure(style='Dark.TFrame')

    # Estilos do ttk
    style.configure('Dark.TFrame', background=BG_COLOR)
    style.configure('Dark.TLabel', background=BG_COLOR, foreground=FG_COLOR, font=('Segoe UI', 9))
    style.configure('Dark.TButton', background=BTN_COLOR, foreground=FG_COLOR, font=('Segoe UI', 10, 'bold'))
    style.map('Dark.TButton', background=[('active', '#555555')])
    style.configure('Accent.TButton', background=ACCENT_COLOR, foreground=FG_COLOR, font=('Segoe UI', 10, 'bold'))
    style.map('Accent.TButton', background=[('active', '#005A9E')])
    style.configure('Dark.Horizontal.TProgressbar', troughcolor=BTN_COLOR, background=ACCENT_COLOR, bordercolor=FG_COLOR)
    
    # Aplica o estilo a cada widget
    theme_frame.configure(style='Dark.TFrame')
    label_arquivo.configure(style='Dark.TLabel')
    btn_selecionar.configure(style='Dark.TButton')
    btn_transcrever.configure(style='Accent.TButton') 
    btn_claro.configure(style='Dark.TButton')
    btn_escuro.configure(style='Dark.TButton')
    btn_sair.configure(style='Dark.TButton')
    progress_bar.configure(style='Dark.Horizontal.TProgressbar')

def aplicar_modo_claro():
    # Cores (padrão do ttk ou customizadas)
    BG_COLOR = '#F0F0F0' # Cor de fundo padrão do sistema
    FG_COLOR = 'black'
    
    # Aplica cores ao root e frames
    root.configure(bg=BG_COLOR)
    main_frame.configure(style='TFrame') # Estilo padrão do Frame

    # Estilos do ttk (voltando ao padrão 'clam')
    style.configure('TFrame', background=BG_COLOR)
    style.configure('TLabel', background=BG_COLOR, foreground=FG_COLOR, font=('Segoe UI', 9))
    style.configure('TButton', font=('Segoe UI', 10, 'bold')) # Botão padrão do tema
    style.configure('TProgressbar') # Barra de progresso padrão

    # Aplica o estilo a cada widget
    theme_frame.configure(style='TFrame')
    label_arquivo.configure(style='TLabel')
    btn_selecionar.configure(style='TButton')
    btn_transcrever.configure(style='TButton')
    btn_claro.configure(style='TButton')
    btn_escuro.configure(style='TButton')
    btn_sair.configure(style='TButton')
    progress_bar.configure(style='TProgressbar')

#instancia do TK
root = tk.Tk()
root.title("Transcritor de Áudio")
root.geometry("550x420") 
root.resizable(False, False)

# Centraliza a janela na tela
window_width = 550
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# --- Variáveis ---
progress_var = tk.IntVar()
caminho_var = tk.StringVar()
texto_transcrito = ""
caminho_var.set("Nenhum arquivo selecionado")

# --- Estilo ---
style = ttk.Style(root)
style.theme_use('clam')

# --- Widgets ---
# Frame principal para organizar o conteúdo
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(expand=True, fill='both')

# Botão para selecionar o arquivo
btn_selecionar = ttk.Button(main_frame, text="Selecionar Arquivo de Áudio", command=selecionar_arquivo)
btn_selecionar.pack(pady=10, fill='x', ipady=4)

# Label para exibir o caminho do arquivo selecionado
label_arquivo = ttk.Label(main_frame, textvariable=caminho_var, wraplength=400, justify="center")
label_arquivo.pack(pady=10)

# Barra de progresso
progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=300, mode="determinate", variable=progress_var)
progress_bar.pack(pady=15)

# Botão para iniciar a transcrição
btn_transcrever = ttk.Button(main_frame, text="Transcrever", command=iniciar_transcritor)
btn_transcrever.pack(pady=10, fill='x', ipady=4)

# --- Frame para os botões de tema ---
theme_frame = ttk.Frame(main_frame)
theme_frame.pack(pady=(20, 0), fill='x')

# Botão CLARO (com o comando para chamar a função)
btn_claro = ttk.Button(theme_frame, text="Modo Claro", command=aplicar_modo_claro)
btn_claro.pack(side='left', fill='x', expand=True, padx=(0, 5))

# Botão ESCURO (com o comando para chamar a função)
btn_escuro = ttk.Button(theme_frame, text="Modo Escuro", command=aplicar_modo_escuro)
btn_escuro.pack(side='right', fill='x', expand=True, padx=(5, 0))

# Botão para sair
btn_sair = ttk.Button(main_frame, text="Sair", command=root.destroy)
btn_sair.pack(pady=(10, 0), fill='x', ipady=4)

# Inicia a aplicação no modo claro por padrão
aplicar_modo_claro()

#Loop do programa
root.mainloop()