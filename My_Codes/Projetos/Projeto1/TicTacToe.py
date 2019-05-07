# encoding: utf-8
tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print(tab)


def display_board(board):
  print('|----------------------------------##----------------------------------|')
  print('-------------------------------INÍCIO DO JOGO---------------------------')
  print('|----------------------------------##----------------------------------|')
  mark_ = mark()
  count = 1
  # print(mark_)
  end = False
  while end == False:
    count +=1
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]) 
        
    p = played(count)
    # print('print de p: %s' %p)
    if   p[1] == mark_[0]:
      board[p[0]-1] = p[1]
    elif p[1]== mark_[1]:
      board[p[0]-1] = p[1]
      
    # print('print de p: %s' %p)
    # print('print do tabuleiro: %s '%board)
    print('|----------------------------------##----------------------------------|')
    print('|----------------------------------##----------------------------------|')
    end = endGame(board)
  print('-------------------------------FIM DO JOGO------------------------------')
  print('|----------------------------------##----------------------------------|')
  print('|----------------------------------##----------------------------------|')
  
def mark():
  mark = ['X','O']
  return mark 

def played(vez):
  p1 = 'X'
  p2 = 'O'
  jp = []
  count = vez
  if count % 2 == 0:
    j = int(input('JOGADOR Nº 1\n Onde deseja jogar?'))
    jp.append(j)
    jp.append(p1)
    # print('print de j: %s'%j)
    # print('Saida: %s' %jp)
    return jp
  elif count % 2 != 0:
    j = int(input('JOGADOR Nº 2\n Onde deseja jogar?'))
    jp.append(j)
    jp.append(p2)
    # print('print de j: %s'%j)
    # print('Saida: %s' %jp)
    return jp


def endGame(board):
  mark_ = mark()
  if board[0] == mark_[0] and board[1] == mark_[0] and board[2] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Horizontal 1
    return True
  elif board[3] == mark_[0] and board[4] == mark_[0] and board[5] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Horizontal 2
    return True
  elif board[6] == mark_[0] and board[7] == mark_[0] and board[8] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Horizontal 3
    return True
  elif board[0] == mark_[0] and board[3] == mark_[0] and board[6] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Vertical 1
    return True
  elif board[1] == mark_[0] and board[4] == mark_[0] and board[7] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Vertical 2
    return True
  elif board[2] == mark_[0] and board[5] == mark_[0] and board[8] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Vertical 3
    return True
  elif board[0] == mark_[0] and board[4] == mark_[0] and board[8] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Diagonal 1
    return True
  elif board[6] == mark_[0] and board[4] == mark_[0] and board[2] == mark_[0]:
    print('-------JOGADOR Nº1 [X] É O VENCEDOR!----------') #Diagonal 2
    return True
  elif board[0] == mark_[1] and board[1] == mark_[1] and board[2] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Horizontal 1
    return True
  elif board[3] == mark_[1] and board[4] == mark_[1] and board[5] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Horizontal 2
    return True
  elif board[6] == mark_[1] and board[7] == mark_[1] and board[8] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Horizontal 3
    return True
  elif board[0] == mark_[1] and board[3] == mark_[1] and board[6] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Vertical 1
    return True
  elif board[1] == mark_[1] and board[4] == mark_[1] and board[7] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Vertical 2
    return True
  elif board[2] == mark_[1] and board[5] == mark_[1] and board[8] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Vertical 3
    return True
  elif board[0] == mark_[1] and board[4] == mark_[1] and board[8] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Diagonal 1
    return True
  elif board[6] == mark_[1] and board[4] == mark_[1] and board[2] == mark_[1]:
    print('-------JOGADOR Nº2 [O] É O VENCEDOR!----------') #Diagonal 2
    return True
  return False
  
# Chamada inicial
display_board(tab)
