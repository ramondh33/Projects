#########################################
#
# Tic Tac Toe Game Mile Stone Project
#
'''
print intro to game and player chooses O or X
program then randomly chooses who goes first
program asks player to enter position
program places an X or O in that position depending on whos turn it is
program then asks other player to enter position etc
when three of the same input match in same line player wins
program asks players to play again or exit
'''
#########################################


import random
# First write player functions returns player 1 and player 2
def player_input(player):
    player1 = player.random()
    print(player1)

    while player1 == None:
        player1 = input("Please choose 'O' or 'X': ")
        if player1.upper() == 'O':
            player2 = 'X'
        elif player1.upper() == 'X':
            player2 = 'O'
        else:
            print("Please pick one of the choice characters.")
            player1 = None

    return player1,player2

# Game board position using list
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Print the game board
def display_game(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('\n')
    print("Welcome to my Tic Tac Toe game!")



# Input player position choice
def player_position(player1,player2):
    choice = [player1,player2]
    choice.random()
    return choice

# Replacing position with corresponding letter
#def replacement():

player1 = None
player2 = None
player = [player1,player2]
player_input(player)
display_game(board)
player_position(player1,player2)
