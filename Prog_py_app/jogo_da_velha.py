import flet as ft

class JogoDaVelha:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Jogo da Velha"
        self.page.bgcolor = "#0d47a1"

        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.mensagem = ft.Text(size=20, weight="bold")

        # Placar
        self.placar_x = 0
        self.placar_o = 0
        self.texto_placar = ft.Text("", size=18, weight="bold")

        self._construir_interface()
        self._reiniciar_jogo(None)  # inicia com o tabuleiro limpo

    def _construir_interface(self):
        self._atualizar_placar()

        self.celulas = [[self._criar_celula(i, j) for j in range(3)] for i in range(3)]

        tabuleiro_ui = ft.Column(
            [ft.Row(self.celulas[i], alignment="center") for i in range(3)],
            alignment="center",
            spacing=5
        )

        reiniciar_btn = ft.ElevatedButton(
            text="🔄 Reiniciar",
            on_click=self._reiniciar_jogo,
            bgcolor="#2196f3",
            color="white"
        )

        layout = ft.Column(
            [
                ft.Text("Jogo da Velha", size=30, weight="bold", text_align="center"),
                self.texto_placar,
                tabuleiro_ui,
                self.mensagem,
                reiniciar_btn
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        )

        self.page.controls.clear()
        self.page.add(layout)
        self.page.update()

    def _criar_celula(self, i, j):
        return ft.Container(
            width=100,
            height=100,
            bgcolor="white",
            border_radius=5,
            alignment=ft.alignment.center,
            content=ft.Text("", size=32, weight="bold"),
            on_click=lambda e: self._marcar_celula(i, j)
        )

    def _marcar_celula(self, i, j):
        if self.tabuleiro[i][j] == "" and self.mensagem.value == "":
            self.tabuleiro[i][j] = self.jogador_atual
            self.celulas[i][j].content.value = self.jogador_atual
            self.celulas[i][j].bgcolor = "#9c27b0" if self.jogador_atual == "X" else "#ff9800"

            if self._verificar_vitoria(self.jogador_atual):
                self.mensagem.value = f"🎉 {self.jogador_atual} venceu!"
                if self.jogador_atual == "X":
                    self.placar_x += 1
                else:
                    self.placar_o += 1
                self._atualizar_placar()

            elif self._verificar_empate():
                self.mensagem.value = "😲 Empate!"
            else:
                self._alternar_jogador()

            self.page.update()

    def _alternar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def _verificar_vitoria(self, jogador):
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)) or \
               all(self.tabuleiro[j][i] == jogador for j in range(3)):
                return True

        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True

        return False

    def _verificar_empate(self):
        return all(self.tabuleiro[i][j] != "" for i in range(3) for j in range(3))

    def _reiniciar_jogo(self, e):
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.mensagem.value = ""

        for i in range(3):
            for j in range(3):
                self.celulas[i][j].content.value = ""
                self.celulas[i][j].bgcolor = "white"

        self.page.update()

    def _atualizar_placar(self):
        self.texto_placar.value = f"🏆 Placar - X: {self.placar_x} | O: {self.placar_o}"


def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    JogoDaVelha(page)

ft.app(target=main, view=ft.AppView.FLET_APP)

