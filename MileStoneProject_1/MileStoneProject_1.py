# Tic Tac Toe Game

def intro():
    print("********** Welcome To Tic Tac Toe! **********")
    print("   ********** Created by Ramon **********   ")

def gameMenu():
    choice = 0
    while choice != 2:
        print("1. Start Game")
        print("2. Quit Game")
        try:
            choice = int(input("What would you like to do? "))
        except:
            print("\nInvalid choice. Please try again!\n")
            continue
        if choice == 2:
            print("\nThanks for playing! Goodbye!")
            exit()

        return choice

def player(choice):
    playerOne = 0
    playerTwo = 0
    playerOne = input("Please choose X or O: ")

    playerOne = playerOne.upper()

    if playerOne == "X":
        playerTwo = "O"
        return playerOne,playerTwo

    elif playerOne == "O":
        playerTwo = "X"
        return playerOne,playerTwo

def gameBoard(board):
    print("\n")
    print("   |   |   ")
    print(" "+board[1],"| "+board[2],"| "+board[3]," ")
    print("-------------")
    print("   |   |   ")
    print(" "+board[4],"| "+board[5],"| "+board[6]," ")
    print("-------------")
    print("   |   |   ")
    print(" "+board[7],"| "+board[8],"| "+board[9]," ")
    print("\n")

def position(playerOne):
    try:
        playerPosition = int(input("Enter position: "))
    except:
      print("Invalid Input")

    for Position in board:

        if board[playerPosition] != " ":
            print("Position taken, please choose an empty position!")

        else:
            board[playerPosition] = playerOne
            return board

def position(playerTwo):
    try:
        playerPosition = int(input("Enter position: "))
    except:
      print("Invalid Input")

    for Position in board:
        board[playerPosition] = playerTwo

    if board[playerPosition] != " ":
        print("Position taken, please choose an empty position!")

    else:
        return board

# Left off at players picking positions then having the program place it on the board and reprinting updated board
choice = 0

board = ["0", " ", " "," "," "," "," "," "," "," "]

gameMenu()

gameBoard(board)



position(playerOne)

position(playerTwo)

gameBoard(board)
