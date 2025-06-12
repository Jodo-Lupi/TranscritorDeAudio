from tkinter import messagebox
import speech_recognition as sr
import math

#função responsavel por transcrever o áudio
def transcrever_audio(nome_arquivo, callback=None):
    r = sr.Recognizer()
    texto = ""

    with sr.AudioFile(nome_arquivo) as source:
        r.adjust_for_ambient_noise(source)

        if (source.DURATION>59):
            vezes = int(math.ceil(source.DURATION/30))
            for chunk in range(vezes):
                try: 
                    audio = r.record(source, duration=30)
                    parte = r.recognize_google(audio, language="pt-BR")
                    texto += parte + ", "

                    # Calcula e atualiza o progresso
                    if callback:
                        progresso = int(((chunk + 1) / vezes) * 100)
                        callback(progresso)
                except sr.UnknownValueError:
                    messagebox.showerror("Erro", "Não foi possível transcrever o áudio.")
                except sr.RequestError:
                    messagebox.showerror("Erro", "Não foi possível conectar-se a API do google.")
        else:
            try:
                audio = r.record(source)
                texto = r.recognize_google(audio, language="pt-BR")

                if callback:
                    callback(100)
            except sr.UnknownValueError:
                messagebox.showerror("Erro", "Não foi possível transcrever o áudio.")
            except sr.RequestError:
                messagebox.showerror("Erro", "Não foi possível conectar-se a API do google.")
    return texto