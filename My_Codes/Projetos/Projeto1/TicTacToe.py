# encoding: utf-8
# tab = ['1', '2', '3', '4','5', '6', '7', '8', '9']
tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print(tab)


def display_board(board):
  mark_ = mark()
  count = 0
  print(mark_)
  end = False
  # end = endGame(board)
  while end == False:
    count +=1
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]) 
    
    
    p = played(count)
    # p = [posição, jogador]
    print('print de p: %s' %p)
    if p[1] == mark_[0]:
      board[p[0]] = p[1]
    elif p[1]== mark_[1]:
      board[int(p[0])-1] = [p[1]]
      
    print('----------------------------------')
    print('----------------------------------')
    print('print de p: %s' %p)
    print('print do tabuleiro: %s '%board)
    print('----------------------------------')
    print('----------------------------------')
    # end = endGame(board)
    
def mark():
  mark = ['X','O']
  return mark 

def played(vez):
  p1 = 'X'
  p2 = 'O'
  jp = []
  count = vez
  if count % 2 != 0:
    j = input('JOGADOR Nº 1\n Onde deseja jogar?')
    
    jp.append(j)
    jp.append(p1)
    print('print de j: %s'%j)
    print('Saida: %s' %jp)
    return jp
  else:
    j = input('JOGADOR Nº 2\n Onde deseja jogar?')
    
    jp.append(j)
    jp.append(p2)
    print('print de j: %s'%j)
    print('Saida: %s' %jp)
    return jp


# def endGame(board):
#   print('Passou')
#   mark_ = mark()
#   print([mark_,mark_,mark_,mark_,' ',' ',' ',' '])
#   print(mark_)
#   if board == [mark_,mark_,mark_,mark_,' ',' ',' ',' ']:
#     return True
#   return False
  
# Chamada inicial
display_board(tab)
