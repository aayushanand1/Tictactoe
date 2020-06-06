#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from IPython.display import clear_output

def display_x(board):
    clear_output()
    
    print('    |    |')
    print('  '+ board[7]  + ' | ' +board[8] + '  | ' + board[9])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  '+ board[4]  + ' | ' +board[5] + '  | ' + board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  '+ board[1]  + ' | ' +board[2] + '  | ' + board[3])
    print('    |    |')
    


# In[2]:


test = ['#','X','o','X','X','X','o','o','X','X']
display_x(test)


# In[3]:


def Assign():
    marker = ''
        
    while not (marker == 'X'or marker == 'O'):
        marker = input('Player 1: Do you want X or O?\n').upper()
        
        if marker == 'X':
            return('X', 'O')
        else:
            return ('O', 'X')
        


# In[4]:


player input(test)


# In[5]:


Player_in(test)


# In[6]:


Assign()


# In[7]:


def Pos( board, marker, position):
    board[position] = marker


# In[8]:


Pos(test,"@", 6)
display_x(test)


# In[9]:


def win( board,mark):
    return((board[7]== mark and board[8] == mark and board[9]== mark)
           or 
           (board[4]== mark and board[5] == mark and board[6]== mark)
           or
           (board[1]== mark and board[2] == mark and board[3]== mark)
           or(board[7]== mark and board[4] == mark and board[1]== mark)
           or
           (board[8]== mark and board[5] == mark and board[2]== mark)
           or
           (board[9]== mark and board[6] == mark and board[3]== mark)
           or
           (board[7]== mark and board[5] == mark and board[3]== mark)
           or
           (board[1]== mark and board[5] == mark and board[9]== mark))


# In[10]:


win(test, 'X')


# In[11]:


import random
def first_player():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[12]:


def empty( board, position):
    return board[position]== ' '


# In[13]:


def board_check(board):
    for i in range (1,10):
        if empty(board,i):
            return False
        else:
            return True


# In[14]:


def Player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not empty(board,position):
        position= int(input('choose your next position: (1-9) ')) 
    return position


# In[15]:


def replay():
    return input('Do you want to play again? Enter Yes or NO: ').lower().startswith('y')


# In[ ]:


print('Welcome to Tic Tac Toe')

while True:
    theBoard= [' '] * 10
    player1_marker, player2_marker = Assign()
    turn = first_player()
    print (turn + ' will go first,')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on= False
    
    while game_on:
        if turn == 'Player 1':
            display_x(theBoard)
            position = Player_choice(theBoard)
            Pos(theBoard, player1_marker, position)
            if win(theBoard,player1_marker):
                display_x(theBoard)
                print('congratulations! player 1 has won!')
                game_on= False
            else:
                if board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_x(theBoard)
            position = Player_choice(theBoard)
            Pos(theBoard, player2_marker, position)
           
            if win(theBoard,player2_marker):
                display_x(theBoard)
                print('congratulations! Player 2 has won!')
                game_on= False
            else:
                 if board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
               
            
                 else:
                    turn = 'Player 1'
    if not replay():
        break
        
        


# In[ ]:





# In[ ]:





# In[ ]:




