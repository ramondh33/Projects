# Tic Tac Toe Game

def intro():
    print("********** Welcome To Tic Tac Toe! **********")
    print("   ********** Created by Ramon **********   ")

def gameMenu():
    playerOne = 0
    playerTwo = 0
    choice = 0
    while choice != 2:
        print("1. Start Game")
        print("2. Quit Game")
        try:
            choice = int(input("What would you like to do? "))
        except:
            print("\nInvalid choice. Please try again!\n")
            continue

        if choice == 1:
            playerOne = input("Player one please choose X or O: ")
            playerOne = playerOne.upper()

        if playerOne == "X":
           playerTwo = "O"
           break
        elif playerOne == "O":
           playerTwo = "X"
           break
        
        else:
            print("Thanks for playing!")
            break

       

board = ["1", " ", " "," "," "," "," "," "," "," "]

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

def position():
    try:
        playerPosition = int(input("Enter position: "))
    except:
      print("Invalid Input")

    for Position in board:
        board[playerPosition] = "X"
# Left off at players picking positions then having the program place it on the board and reprinting updated board
gameMenu()
while True:
    gameBoard(board)
    position()
#while playerOnePosition == 0:
#    try:
 #       playerOnePosition = int(input("Enter a number from 1-9 to choose you position: "))
  #  except:
   #     print("Invalid choice")