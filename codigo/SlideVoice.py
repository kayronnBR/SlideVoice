import os
import json
import pyaudio
import pyautogui
import sys
import subprocess
from vosk import Model, KaldiRecognizer

# --- CONFIGURAÇÕES DE CAMINHO E PALAVRAS ---
# Certifique-se de que o caminho abaixo corresponde ao seu usuário
BASE_DIR = "/home/kayronn/passador_voz"
MODEL_PATH = os.path.join(BASE_DIR, "model")

# Palavras formais e longas para evitar acionamentos acidentais
PALAVRA_AVANCAR = "prosseguir"
PALAVRA_VOLTAR = "retroceder"

# Gramática restritiva para o modelo focar apenas nestes comandos
GRAMATICA = f'["{PALAVRA_AVANCAR}", "{PALAVRA_VOLTAR}", "[unk]"]'

# --- FUNÇÕES DE FEEDBACK E NOTIFICAÇÃO ---
def emitir_som(tipo):
    """ Emite bipes sutis para confirmação de comandos e início """
    try:
        if tipo == "avancar":
            # Bipe agudo (800Hz) para avançar
            subprocess.Popen([
                "play", "-v", "0.2", "-q", "-n", "synth", "0.04", "sine", "800", 
                "fade", "0.01", "0.04", "0.01"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif tipo == "voltar":
            # Bipe grave (400Hz) para voltar
            subprocess.Popen([
                "play", "-v", "0.2", "-q", "-n", "synth", "0.04", "sine", "400", 
                "fade", "0.01", "0.04", "0.01"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif tipo == "inicio":
            # Som de sucesso ao carregar (dois bipes rápidos)
            subprocess.Popen([
                "play", "-v", "0.3", "-q", "-n", "synth", "0.1", "sine", "500", "sine", "800", "delay", "0", "0.1"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def notificar_sistema(titulo, mensagem):
    """ Mostra um pop-up visual no Linux Mint/Ubuntu """
    try:
        subprocess.Popen(["notify-send", titulo, mensagem])
    except Exception:
        pass

# --- INICIALIZAÇÃO DO MOTOR DE VOZ ---
if not os.path.exists(MODEL_PATH):
    print(f"❌ ERRO: Pasta do modelo não encontrada em: {MODEL_PATH}")
    sys.exit(1)

print("⌛ Carregando IA local (Vosk)...")
try:
    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, 16000, GRAMATICA)
except Exception as e:
    print(f"❌ Erro ao inicializar modelo: {e}")
    sys.exit(1)

p = pyaudio.PyAudio()
try:
    stream = p.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=16000, 
        input=True, 
        frames_per_buffer=8000
    )
    stream.start_stream()
except Exception as e:
    print(f"❌ Erro ao acessar o microfone: {e}")
    sys.exit(1)

# Feedback de que o sistema está pronto
print("\n" + "═"*45)
print("🚀 PASSADOR DE SLIDES PROFISSIONAL ATIVO")
print(f"  • Comando Avançar: '{PALAVRA_AVANCAR.upper()}'")
print(f"  • Comando Voltar:  '{PALAVRA_VOLTAR.upper()}'")
print("═"*45)

emitir_som("inicio")
notificar_sistema("SlideVoice", f"IA Ativa! Diga '{PALAVRA_AVANCAR}' para passar.")

# --- LOOP DE RECONHECIMENTO ---
try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        
        if rec.AcceptWaveform(data):
            resultado = json.loads(rec.Result())
            texto = resultado.get("text", "")

            if texto == PALAVRA_AVANCAR:
                print(f"➡️  [AÇÃO] {PALAVRA_AVANCAR.upper()}")
                emitir_som("avancar")
                pyautogui.press('right')
            
            elif texto == PALAVRA_VOLTAR:
                print(f"⬅️  [AÇÃO] {PALAVRA_VOLTAR.upper()}")
                emitir_som("voltar")
                pyautogui.press('left')

except KeyboardInterrupt:
    print("\n👋 Encerrando o sistema...")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
