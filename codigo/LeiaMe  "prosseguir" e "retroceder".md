# ---

**🎙️ Passador de Slides por Voz (Offline)**

Este projeto permite controlar apresentações de slides (avançar e retroceder) utilizando comandos de voz de forma totalmente offline.

⚠️ **IMPORTANTE:** Este programa utiliza caminhos baseados no diretório do usuário. Em todos os comandos e arquivos (como o executar.sh), **substitua o nome kayronn pelo seu nome de usuário do Linux.**

## ---

**🛠️ Requisitos do Sistema**

Antes de rodar o programa, você precisa instalar as dependências de áudio e simulação de teclado da sua distribuição Linux:

### **1\. Pacotes da Distribuição**

Abra o terminal e execute o comando correspondente à sua distro:

* **Ubuntu / Mint / Debian / Pop\!\_OS:**  
  Bash  
  sudo apt update && sudo apt install python3-pip python3-venv portaudio19-dev libasound2-dev sox libsox-fmt-all

* **Fedora:**

Bash

    sudo dnf install portaudio-devel alsa-lib-devel sox  
    \`\`\`  
\*   \*\*Arch Linux / Manjaro:\*\*  
    \`\`\`bash  
    sudo pacman \-S portaudio alsa-lib sox  
    \`\`\`

\---

\#\# 🚀 Instalação e Configuração

Se você já tem a pasta do programa, siga estes passos para configurar o ambiente Python:

1\.  \*\*Acesse a pasta do projeto:\*\*  
    \`\`\`bash  
    cd /home/SEU\_USUARIO/passador\_voz  
    \`\`\`  
    \*(Lembre-se de trocar \`SEU\_USUARIO\` pelo nome real da sua pasta pessoal).\*

2\.  \*\*Crie o Ambiente Virtual (venv):\*\*  
    \`\`\`bash  
    python3 \-m venv venv  
    \`\`\`

3\.  \*\*Ative o ambiente e instale as bibliotecas Python:\*\*  
    \`\`\`bash  
    source venv/bin/activate  
    pip install vosk pyaudio pyautogui  
    \`\`\`

\---

\#\# 📂 Estrutura de Pastas

Para que o programa funcione, sua pasta deve estar assim:  
\*   \`SlideVoice.py\` (O código principal)  
\*   \`executar.sh\` (O script de inicialização rápida)  
\*   \`model/\` (Pasta contendo os arquivos do modelo Vosk em Português)  
\*   \`venv/\` (Pasta criada no passo anterior)

\---

\#\# ⚡ Como Usar

1\.  \*\*Ajuste o Script de Execução:\*\*  
    Abra o arquivo \`executar.sh\` e certifique-se de que o caminho está correto para o seu usuário:  
      
\`\`\`bash  
    nano executar.sh  
    \# Verifique se está: /home/SEU\_NOME/passador\_voz/...  
    \`\`\`

2\.  \*\*Dê permissão ao arquivo:\*\*  
    \`\`\`bash  
    chmod \+x executar.sh  
    \`\`\`

3\.  \*\*Execute o programa:\*\*  
    \`\`\`bash  
    ./executar.sh  
    \`\`\`

4\.  \*\*Comandos de Voz:\*\*  
    \*   Diga \*\*"prosseguir"\*\* para avançar.  
    \*   Diga \*\*"retroceder"\*\* para retroceder.

\---

\#\# 🔈 Notas  
\*   O programa emite um som discreto (bipe) a cada comando reconhecido.  
\*   Certifique-se de que o microfone está configurado corretamente no painel de controle de som da sua distro.  
\*   Mantenha o foco da janela na sua apresentação de slides após iniciar o script.  
