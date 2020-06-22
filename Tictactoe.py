''' Tic Tac Toe for 2 players in Python '''
import sys
# Made by :Pratham Prasoon
# Twitter @PrassonPratham
   
#Board 
board = [ '0','1','2', '3', '4', '5', '6', '7', '8']

#Current Player = X
player = 'X'

#Displaying which player's turn is next
pseudoPlayer = "X"

#Places that have been filled
slotsFilled = 0


#Draw the Tic Tac Toe Board
def drawBoard():
    print("-------------") 
    print("| " +board[0] + " | " + board[1]+ ' | '+board[2] + ' |')
    print("|-----------|" )
    print("| " +board[3] + " | " +  board[4]+ ' | '+board[5]+ ' |' )
    print("|-----------|"  )
    print("| " +board[6] + " | " +  board[7]+ ' | '+board[8] + ' |')
    print("-------------" ) 
    print(pseudoPlayer+"'s turn")
 
#Check if the game has been won or Tied 
def checkGameWon():
    if board[0] == board[1] == board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[7]==board[4]==board[1] or board[2] ==board[5]==board[8]:
        print("")           
        print("**************")
        print("Game won by " + player)
        print("🎉")
        print("**************")
        sys.exit()
    elif slotsFilled == 9:
        print("")           
        print("**************")
        print("Game Tied")
        print("    -_-")
        print("**************")
        sys.exit()
             
#Game sequence
#Write code here👇     
        
