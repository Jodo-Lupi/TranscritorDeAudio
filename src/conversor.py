import os
import tempfile
from pydub import AudioSegment

#Convertor do arquivo de áudio para .wav
def conversorAutomaticoDeAudio(arquivo_selecionado):
    # Criar um diretório temporário seguro
    temp_dir = tempfile.gettempdir()
    
    # Definir a extensão suportada
    extensoes_suportadas = {
        '.mp3': AudioSegment.from_mp3,
        '.ogg': AudioSegment.from_ogg,
    }

    # Obter a extensão do arquivo
    _, ext = os.path.splitext(arquivo_selecionado)
    ext = ext.lower()

    # Verificar se a extensão é suportada
    if ext in extensoes_suportadas:
        audio = extensoes_suportadas[ext](arquivo_selecionado)
    else:
        # Para formatos não especificados, usar `from_file`
        audio = AudioSegment.from_file(arquivo_selecionado)

    # Criar um caminho para o novo arquivo temporário
    arquivo_temporario = os.path.join(temp_dir, os.path.basename(arquivo_selecionado).replace(ext, '.wav'))

    # Exportar o áudio convertido
    audio.export(arquivo_temporario, format="wav")
    
    return arquivo_temporario  # Retorna o caminho do novo arquivo