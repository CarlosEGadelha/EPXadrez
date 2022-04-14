import chess
import random

class Xadrez:
  def __init__(self):
    self.cores = ["White", "Black"]
    self.ultima_cor = None

  def inicializar(self, estado = None):
    if(estado is None):
      self.board = chess.Board()

  def retorna_estado(self):
    return self.board.copy()

  def jogar(self, acao, simbolo):
    self.board.push_san(acao)
    self.ultima_cor = simbolo
  
  def sucessora(self):
    lista_movimentos = list(self.board.legal_moves)
    return lista_movimentos
          
  def utilidade(self, turno):
    if(self.fim_de_jogo() != ""):
      if (self.fim_de_jogo() == "Empate" or self.fim_de_jogo() == "O jogo acabou"):
        return 0
      else:
        if self.ultima_cor == turno:
          return 1
        else:
          return -1
    
  def fim_de_jogo(self):
    if (self.board.is_checkmate()):
      return "Cheque-Mate"
    if (self.board.is_stalemate()):
      return "Empate" # - Rei sem movimento
    if (self.board.is_insufficient_material()):
      return "Empate" # - Não há peças para cheque-mate
    if (self.board.is_game_over()):
      return "O jogo acabou"
    return ""
      
    def __str__(self):
      return 'value of a = {} value of b =     {}'.format(self.a, self.b)

def minimax(estado, acao, turno, simbolo_agente, guardaMov, copia_estado):
  copia_estado.board = estado.retorna_estado()
  
  if copia_estado.fim_de_jogo() != "":
    return copia_estado.utilidade(simbolo_agente)

  if simbolo_agente == turno:
    utilidade = -1000
    if guardaMov == True:
      copia_estado.jogar(str(acao), turno)
      turno = "Preto"
      utilidade = max(utilidade, minimax(copia_estado, acao, turno, "Branco", False, copia_estado))
      return utilidade
    else:
      acao = random.choice(copia_estado.sucessora())
      copia_estado.jogar(str(acao), turno)
      turno = "Preto"
      utilidade = max(utilidade, minimax(copia_estado, acao, turno, "Branco", False, copia_estado))
      return utilidade
  else:
    utilidade = +1000
    acao = random.choice(copia_estado.sucessora())
    copia_estado.jogar(str(acao), turno)
    turno = "Branco"
    utilidade = min(utilidade, minimax(copia_estado, acao, turno, "Branco", False, copia_estado))
    return utilidade

x = Xadrez()
x.inicializar()

copia_estado = Xadrez()
copia_estado.inicializar()

print(x.board)
print("\n")

jogador_cor = "Branco"
turno = "Branco"

while (not x.fim_de_jogo() != ""):
  while True:
    acao = random.choice(x.sucessora())
    retorno = minimax(x, acao, turno, "Branco", True, copia_estado)
    if retorno >= 0:
      x.jogar(str(acao), turno)
      print("\n")
      print(x.board)
    if not retorno < 0:
      turno = "Preto"
      break
        
  while True:
    acao = random.choice(x.sucessora())
    retorno = minimax(x, acao, turno, "Preto", True, copia_estado)
    if retorno >= 0:
      x.jogar(str(acao), turno)
      print("\n")
      print(x.board)
    if not retorno < 0:
      turno = "Branco"
      break
  
if(x.fim_de_jogo() == "Cheque-Mate"):
  print("O vencedor é " + x.ultima_cor)
else:
  print("Empate") 
