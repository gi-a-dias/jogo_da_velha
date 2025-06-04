
## 📝Jogo da Velha (.exe offline)

````markdown
# 🕹️ Jogo da Velha (Python + Flet)

Um jogo da velha simples, com placar e interface moderna, desenvolvido em Python utilizando a biblioteca Flet — empacotado como executável (.exe), funcionando totalmente offline, sem navegador ou conexão com a internet.

---

## 📦 Como Executar (Windows)

1. **Baixe o arquivo** `jogo_da_velha.exe`  
2. **Dê um duplo clique** para abrir o app  
3. Jogue direto: não precisa instalar nada!

---

## 🎮 Funcionalidades

- Interface em estilo Flutter
- Dois jogadores (X e O)
- Contagem de vitórias
- Verificação automática de vitória ou empate
- Reinício rápido da partida

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Flet (`flet` e `flet-cli`)
- PyInstaller (para empacotar .exe)

---

## 🚀 Como gerar o executável você mesmo

Caso queira gerar novamente:

```bash
pip install flet pyinstaller
pyinstaller jogo_da_velha.py --noconfirm --onefile --noconsole --icon=jogoDaVelha.ico
````

> 💡 Use o modo `view=ft.FLET_APP` no `ft.app()` para que a aplicação funcione offline como app nativo (sem navegador).

---

## 📌 Notas

* Esse aplicativo funciona em **Windows** sem necessidade de instalação de Python.
* Para outras plataformas (Linux, macOS, Android), o código pode ser adaptado ou rodado como web app.

---

## 👨‍💻 Autor

Desenvolvido por
Projeto acadêmico
