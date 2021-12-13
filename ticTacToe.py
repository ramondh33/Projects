# Tic Tac Toe just testing branches using git command
import random

#intro
print("Welcome to Tic Tac Toe!")
print("Created by Ramon.")

#Menu
choice = 0
playerOne = 0
playerTwo = 0
while choice != 'q' or choice != 'Q':
    print("\n1.Start Game\nQ.Quit\n")
    choice = input("What would you like to do? ")

    if choice == '1':
        playerOne = input("Please choose X or O: ")
        playerOne = playerOne.upper()
        if playerOne == 'X':
            playerTwo = 'O'
            break
        else:
            playerTwo = 'X'
            break

    if choice == 'Q' or choice == 'q':
        print("\nThanks for playing. Goodbye!")
        quit()

    else:
        print("\nInvalid Entry!")

playerOne = random.choice(['X','O'])
if playerOne == 'X':
    playerTwo = 'O'
    print(playerOne,"will go first!")
elif playerOne == 'O':
    playerTwo = 'X'
    print(playerOne,"will go first!")

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

print('\n')
print(" "+board[0][0], "|", " "+board[0][1], "|", " "+board[0][2])
print("--------------")

print(" "+board[1][0], "|", " "+board[1][1], "|", " "+board[1][2])
print("--------------")

print(" "+board[2][0], "|", " "+board[2][1], "|", " "+board[2][2])

while True:
    for move1 in board:
        print(playerOne, "where do you want to place your mark? ")
        positionOne = input()

        if positionOne == '1':
            board[0][0] = playerOne

        elif positionOne == '2':
            board[0][1] = playerOne

        elif positionOne == '3':
            board[0][2] = playerOne

        elif positionOne == '4':
            board[1][0] = playerOne

        elif positionOne == '5':
            board[1][1] = playerOne

        elif positionOne == '6':
            board[1][2] = playerOne

        elif positionOne == '7':
            board[2][0] = playerOne

        elif positionOne == '8':
            board[2][1] = playerOne

        elif positionOne == '9':
            board[2][2] = playerOne

        print('\n')
        print(" " + board[0][0], "|", " " + board[0][1], "|", " " + board[0][2])
        print("--------------")

        print(" " + board[1][0], "|", " " + board[1][1], "|", " " + board[1][2])
        print("--------------")

        print(" " + board[2][0], "|", " " + board[2][1], "|", " " + board[2][2])