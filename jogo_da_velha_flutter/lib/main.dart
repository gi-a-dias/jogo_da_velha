import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: JogoDaVelha(),
    debugShowCheckedModeBanner: false,
  ));
}

class JogoDaVelha extends StatefulWidget {
  @override
  _JogoDaVelhaState createState() => _JogoDaVelhaState();
}

class _JogoDaVelhaState extends State<JogoDaVelha> {
  List<List<String>> tabuleiro = List.generate(3, (_) => List.generate(3, (_) => ""));
  String jogadorAtual = "X";
  String mensagem = "";
  int placarX = 0;
  int placarO = 0;

  void _marcarCelula(int i, int j) {
    if (tabuleiro[i][j] == "" && mensagem == "") {
      setState(() {
        tabuleiro[i][j] = jogadorAtual;

        if (_verificarVitoria(jogadorAtual)) {
          mensagem = "🎉 $jogadorAtual venceu!";
          if (jogadorAtual == "X")
            placarX++;
          else
            placarO++;
        } else if (_verificarEmpate()) {
          mensagem = "😲 Empate!";
        } else {
          _alternarJogador();
        }
      });
    }
  }

  void _alternarJogador() {
    jogadorAtual = jogadorAtual == "X" ? "O" : "X";
  }

  bool _verificarVitoria(String jogador) {
    for (int i = 0; i < 3; i++) {
      if (tabuleiro[i].every((cell) => cell == jogador)) return true;
      if ([tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]].every((cell) => cell == jogador)) return true;
    }
    if ([tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]].every((cell) => cell == jogador)) return true;
    if ([tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]].every((cell) => cell == jogador)) return true;

    return false;
  }

  bool _verificarEmpate() {
    for (var linha in tabuleiro) {
      if (linha.contains("")) return false;
    }
    return true;
  }

  void _reiniciarJogo() {
    setState(() {
      tabuleiro = List.generate(3, (_) => List.generate(3, (_) => ""));
      jogadorAtual = "X";
      mensagem = "";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF0d47a1),
      appBar: AppBar(
        title: Text("Jogo da Velha"),
        backgroundColor: Color(0xFF0d47a1),
        centerTitle: true,
        elevation: 0,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("\uD83C\uDFC6 Placar - X: $placarX | O: $placarO",
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white)),
            SizedBox(height: 20),
            Column(
              children: List.generate(3, (i) {
                return Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: List.generate(3, (j) {
                    return GestureDetector(
                      onTap: () => _marcarCelula(i, j),
                      child: Container(
                        width: 100,
                        height: 100,
                        margin: EdgeInsets.all(5),
                        decoration: BoxDecoration(
                          color: tabuleiro[i][j] == "X"
                              ? Colors.purple
                              : tabuleiro[i][j] == "O"
                                  ? Colors.orange
                                  : Colors.white,
                          borderRadius: BorderRadius.circular(5),
                        ),
                        child: Center(
                          child: Text(
                            tabuleiro[i][j],
                            style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ),
                    );
                  }),
                );
              }),
            ),
            SizedBox(height: 20),
            Text(mensagem, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white)),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _reiniciarJogo,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blue),
              child: Text("🔄 Reiniciar", style: TextStyle(color: Colors.white)),
            )
          ],
        ),
      ),
    );
  }
}
