'''
import flet as ft
from flet import Alignment
from functools import partial

class JogoDaVelha:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "JOGO DA VELHA"#alterado
        self.page.bgcolor = "#eceff1" #alterado
        self._tela_inicial()

        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.mensagem = ft.Text(size=20, weight="bold",color="#455a64")

        # Placar
        self.placar_x = 0
        self.placar_o = 0
        self.texto_placar = ft.Text("", size=18, weight="bold",color="#212121")


#abre uma tela inicial     
    def _tela_inicial(self):
        btn_iniciar = ft.ElevatedButton(
            text= "🎮 COMEÇAR PARTIDA",
            width = 200,
            height=50,
            bgcolor="#4caf50",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=25),
                elevation=4
            ),
            on_click=self._mostrar_jogo
        )
        
        tela = ft.Column(
             [
                ft.Text("TIC TAC TOE",size = 40,weight="bold",color="#0288d1"),
                btn_iniciar
             ],
             alignment = "center",
             horizontal_alignment="center",
             spacing=30
        )
        
        self.page.controls.clear()
        self.page.add(tela)
        self.page.update()
         
             
        
    def _mostrar_jogo(self,e):
        self._construir_interface()
        self._reiniciar_jogo(None)

    def _construir_interface(self):
        self._atualizar_placar()

        self.celulas = [[self._criar_celula(i, j) for j in range(3)] for i in range(3)]

        tabuleiro_ui = ft.Column(
            [ft.Row(self.celulas[i], alignment="center") for i in range(3)],
            alignment="center",
            spacing=5
        )

        reiniciar_btn = ft.ElevatedButton(
            text="🔄 REINICIAR",#alterado
            on_click=self._reiniciar_jogo,
            bgcolor="#26a69a", #alterado 
            color="white",
            width=150, #alterado 
            height=50,#alterado 
            style=ft.ButtonStyle(     #alterado 
                shape=ft.RoundedRectangleBorder(radius=30),   #alterado 
                elevation=5  #alterado 
            )
        ) 

        layout = ft.Column(
            [
                ft.Text("TIC TAC TOE", size=40, weight="bold", text_align="center",color="#0288d1"),#alterado
                self.texto_placar,
                tabuleiro_ui,
                self.mensagem,
                reiniciar_btn
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=30#alterado
        )

        self.page.controls.clear()
        self.page.add(layout)
        self.page.update()

    def _criar_celula(self, i, j):
        return ft.Container(
            width=120,#tamanho da celula
            height=120,#tamanho da celula
            bgcolor="white",
            border_radius=10,
            #alignment=Alignment.center(),  # esta linha não é reconhecido quando rodo(só roda sem) 
            content=ft.Text("",
                            size=80,#altera o tamanho do x e o
                            weight="bold",
                            color="#607d8b",
                            text_align=ft.TextAlign.CENTER #centraliza o x e o 

                            ),
            on_click=lambda e: self._marcar_celula (i, j),
            #border=ft.border.all(2,color="#78909c"),
            shadow=ft.BoxShadow(color="#cfd8dc",blur_radius=8,spread_radius=3)
           
        )

    def _marcar_celula(self, i, j):
        if self.tabuleiro[i][j] == "" and self.mensagem.value == "":
            self.tabuleiro[i][j] = self.jogador_atual
            self.celulas[i][j].content.value = self.jogador_atual
            self.celulas[i][j].bgcolor = "#9c27b0" if self.jogador_atual == "X" else "#ff9800"

            if self._verificar_vitoria(self.jogador_atual):
                self.mensagem.value = f"🎉 {self.jogador_atual} VENCEU!"
                if self.jogador_atual == "X":
                    self.placar_x += 1
                else:
                    self.placar_o += 1
                self._atualizar_placar()
            elif self._verificar_empate():
                self.mensagem.value = "😲 EMPATE!"#alterado
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
        self.texto_placar.value = f"🏆 PLACAR - X: {self.placar_x} | O: {self.placar_o}"

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    JogoDaVelha(page)

ft.app(target=main)

'''