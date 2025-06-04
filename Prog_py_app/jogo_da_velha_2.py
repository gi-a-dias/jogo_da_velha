import flet as ft

class JogoDaVelha:
    def __init__(self, page: ft.Page):
        self.page = page
        self.num_partidas = 1
        self.partidas_jogadas = 0


        
        # Placar
        self.jogador_atual= "X"
        self.placar_x = 0
        self.placar_o = 0
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.texto_placar = ft.Text("",size = 18, weight="bold",color="#212121")
        self.celulas = [[None for _ in range(3)] for _ in range(3)]
        self.mensagem = ft.Text("",size=20, weight="bold",color="#455a64")
        self.btn_continuar = None


        
        #nome
        self.page.title = "JOGO DA VELHA"
        self.page.bgcolor = "#eceff1" 
        self._tela_inicial()


#abre a tela inicial     
    def _tela_inicial(self,e=None):
        btn_iniciar = ft.ElevatedButton(
            text= "🎮   INICIAR",
            on_click = self._partidas_,
            width = 200,
            height=50,
            bgcolor="#4caf50",
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=25),
                elevation=4
            )
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

#abre a segunda tela
    def _partidas_(self, e = None):
        self.input_partidas_ = ft.TextField(label = "",width = 250,value = "1")
        self.info_text = ft.Text("")
        
        def bloqueio(e):
            valor_str = self.input_partidas_.value.strip()
            if valor_str.isdigit() and int(valor_str) > 0:
                self.num_partidas = int(valor_str)
                self.partidas_jogadas = 0
                self.placar_x = 0
                self.placar_o = 0
                self._mostrar_jogo()
            else:
                self.info_text.value = "⚠️ ESCOLHA UM NUMERO MAIOR QUE ZERO⚠️ "
                self.info_text.color = "#d32f2f"
                self.info_text.size = 10
                self.info_text.weight = "bold"
                self.page.update()

        

        btn_confirmar = ft.ElevatedButton( text = "INICIAR PARTIDA", on_click = bloqueio)
           

        tela = ft.Column(
            [
                ft.Text("MELHOR DE:", size = 30 , weight = "bold",color = "#0288d1"),
                self.input_partidas_,
                btn_confirmar,
                self.info_text
             ],
             alignment = "center",
             horizontal_alignment="center",
             spacing = 30
            
            
                
        )

        self.page.controls.clear()
        self.page.add(tela)
        self.page.update()


#abre a terceira tela         
    def _mostrar_jogo(self,e=None):
        self.btn_continuar = None
        self._construir_interface()
        self._limpar()

    def _construir_interface(self):
        self._atualizar_placar()

        for i in range(3):
            for j in range(3):
                if self.celulas[i][j] is None:
                    self.celulas[i][j] = ft.Container(
                        width=120, 
                        height=120,
                        bgcolor = "white",
                        border_radius = 10,
                        content = ft.Text(
                            "",
                            size = 80,
                            weight="bold",
                            color="#607d8b",
                            text_align=ft.TextAlign.CENTER
                        ),
                        on_click = lambda e, x=i, y=j: self._marcar_celula(x,y ),
                        shadow=ft.BoxShadow(color="#cfd8dc", blur_radius=8, spread_radius=3)
                    )
                    
        tabuleiro_ui = ft.Column(
            [ft.Row(self.celulas[i], alignment="center") for i in range(3)],
            alignment="center",
            spacing=5
            
        )

        

        controls = [
                ft.Text("TIC TAC TOE", size=40, weight="bold", text_align="center",color="#0288d1"),
                self.texto_placar,
                tabuleiro_ui,
                self.mensagem,
        ]
        if self.btn_continuar:
            controls.append(self.btn_continuar)
            
        layout = ft.Column(    
            controls,
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        )

        self.page.controls.clear()
        self.page.add(layout)
        self.page.update()

    def _limpar(self):
        self.tabuleiro=[["" for _ in range (3) ] for _ in range (3) ]
        self.jogador_atual = "X"
        self.mensagem.value = ""
        self.btn_continuar = None

        for i in range(3):
            for j in range(3):
                self.celulas[i][j].content.value = ""
                self.celulas[i][j].bgcolor="white"
        self._construir_interface()
        

    def _marcar_celula(self, i, j):
        if self.tabuleiro[i][j] == "" and self.mensagem.value == "":
            self.tabuleiro[i][j] = self.jogador_atual
            self.celulas[i][j].content.value = self.jogador_atual
            self.celulas[i][j].bgcolor = "#9c27b0" if self.jogador_atual == "X" else "#ff9800"



#vencedor
            if self._verificar_vitoria(self.jogador_atual):
                if self.jogador_atual == "X":
                    self.placar_x += 1
                else:
                    self.placar_o += 1
                self._atualizar_placar()


                self.mensagem.value = f"🎉 {self.jogador_atual} VENCEU!"
                self.partidas_jogadas +=1
                self._botao_continuar()
                return
            

                
#empate               
              
            if self._verificar_empate():
               self.mensagem.value = "😲 EMPATE!"
               self.partidas_jogadas +=1
               self._botao_continuar()
               return

                
            self._alternar_jogador()
            self.page.update()

    def _alternar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def _verificar_vitoria(self, jogador):
        for z in range(3):
            if all(self.tabuleiro[z][j] == jogador for j in range(3)) or \
               all(self.tabuleiro[j][z] == jogador for j in range(3)):
                return True

        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True

        return False

    def _verificar_empate(self):
        return all(self.tabuleiro[i][j] != "" for i in range(3) for j in range(3))

    def _atualizar_placar(self):
        self.texto_placar.value = f"🏆 PLACAR - X: {self.placar_x} | O: {self.placar_o}"
        self.page.update()
        
    def _botao_continuar(self):
        texto_botao = "PROXIMA PARTIDA" if self.partidas_jogadas < self.num_partidas else "FIM DE JOGO"
        self.btn_continuar = ft.ElevatedButton(
            text = texto_botao,
            on_click=self._continuacao,
            bgcolor="#0288d1",
            color="white",
            width=200,
            height=50
        )
        self._construir_interface()
        
    def _continuacao(self, e):
        if self.partidas_jogadas < self.num_partidas:
           self._limpar()
        else:
            self._tela_final()
        
#abre a tela final
    def _tela_final(self, e=None):
        texto_final= ft.Text(
            f"🏁FIM DO MELHOR DE {self.num_partidas}🏁",
            size = 28,
            weight = "bold",
            color = "green",
            text_align= "center"
        )

        criadores = ft.Column(
             [
                 ft.Text("CRIADORES DO TIC TAC TOE:",size=24,weight="bold",color="blue",text_align="center"),
                 ft.Text("GIOVANNA ALMEIDA DIAS",size = 20,color= "blue"),
                 ft.Text("LAIS DE PAULA CARNEIRO",size = 20,color= "blue"),
                 ft.Text("MIGUEL RODRIGUES ARAUJO",size = 20,color= "blue"),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=5
                        

        )
        
        btn_reiniciar = ft.ElevatedButton(
            text = "VOLTAR AO INICIO",
            on_click=self._tela_inicial,
            bgcolor ="#4caf50",
            color="white",
            width = 200,
            height = 50
        )

        layout = ft.Column(
            [
                texto_final,
                criadores,
                btn_reiniciar
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing = 30

         )

        self.page.controls.clear()
        self.page.add(layout)
        self.page.update()
    
            

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    JogoDaVelha(page)

ft.app(target=main)

