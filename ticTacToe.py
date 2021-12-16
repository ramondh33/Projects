# Tic Tac Toe
import random

# Function to continuously ask for position input
def userPositionInput(board,mark1):

    for move in board:
        print(f"\nwhere do you want to place {mark1}? ")
        position = input()
        
        isValid(int(position))
        
        if position == '1':
            board[0][0] = mark1
            return board

        elif position == '2':
            board[0][1] = mark1
            return board

        elif position == '3':
            board[0][2] = mark1
            return board

        elif position == '4':
            board[1][0] = mark1
            return board

        elif position == '5':
            board[1][1] = mark1
            return board

        elif position == '6':
            board[1][2] = mark1
            return board

        elif position == '7':
            board[2][0] = mark1
            return board

        elif position == '8':
            board[2][1] = mark1
            return board

        elif position == '9':
            board[2][2] = mark1
            return board
        
        else:
            print("\nInvalid Entry!")
            
def userPositionInput(board,mark2):
    
    for move in board:
        print(f"\nwhere do you want to place {mark2}? ")
        position = input()
        
        isValid(int(position))
        
        if position == '1':
            board[0][0] = mark2
            return board

        elif position == '2':
            board[0][1] = mark2
            return board

        elif position == '3':
            board[0][2] = mark2
            return board

        elif position == '4':
            board[1][0] = mark2
            return board

        elif position == '5':
            board[1][1] = mark2
            return board

        elif position == '6':
            board[1][2] = mark2
            return board

        elif position == '7':
            board[2][0] = mark2
            return board

        elif position == '8':
            board[2][1] = mark2
            return board

        elif position == '9':
            board[2][2] = mark2
            return board
        
        else:
            print("\nInvalid Entry!")
        
# Function to display board for players
def displayBoard(board):
    print('\n')
    print(" " + board[0][0], "|", " " + board[0][1], "|", " " + board[0][2])
    print("--------------")
    print(" " + board[1][0], "|", " " + board[1][1], "|", " " + board[1][2])
    print("--------------")
    print(" " + board[2][0], "|", " " + board[2][1], "|", " " + board[2][2])
    
# Checking for valid moves
def isValid(position):
    if not (position >= 1 and position < 10):
        return False
    
    return board[position] == ""            
    
#intro
print("Welcome to Tic Tac Toe!")
print("Created by Ramon.")

#Menu
choice = 0
mark1 = 0
mark2 = 0
while choice != 'q' or choice != 'Q':
    print("\n1.Start Game\nQ.Quit\n")
    choice = input("What would you like to do? ")

    if choice == '1':
        mark1 = input("Please choose X or O: ")
        mark1 = mark1.upper()
        if mark1 == 'X':
            mark2 = 'O'
            break
        else:
            mark2 = 'X'
            break

    if choice == 'Q' or choice == 'q':
        print("\nThanks for playing. Goodbye!")
        quit()

    else:
        print("\nInvalid Entry!")

# App choosing player at random
mark1 = random.choice(['X','O'])
if mark1 == 'X':
    mark2 = 'O'
    print(mark1,"will go first!")
elif mark1 == 'O':
    mark2 = 'X'
    print(mark1,"will go first!")

# Board initialization using 2d list
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Using while loop to continuously ask for player position input. Trying to figure out how to do it with two players.
# Displays board after each position is chosen with updated position.
while True:
    for move in board:
        
        # Printing board after each position update
        displayBoard(board)
        
        # Calling function that applies position to baord based on player input
        userPositionInput(board,mark1)
        
        # Printing board after each position update
        displayBoard(board)

        # Calling function that applies position to baord based on player input
        userPositionInput(board,mark2)
        
        
        